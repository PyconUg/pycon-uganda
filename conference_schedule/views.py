from __future__ import absolute_import
from django.shortcuts import render
from django.http import HttpRequest, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.template import RequestContext
from django.views.generic.detail import DetailView 
from django.shortcuts import get_object_or_404
from hitcount.views import HitCountDetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from next_prev import next_in_order, prev_in_order
from home.models import EventYear
from registration.models import Profile 
from talks.models import Proposal
from .forms import TalkScheduleForm  
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from .models import * 


from datetime import datetime

from .models import Schedule, Day



def schedule(request, year):
    """Renders the schedule page for a specific year."""
    assert isinstance(request, HttpRequest)

    # Fetch the event year or raise 404 if not found
    event_year = get_object_or_404(EventYear, year=year)

    # Check the visibility setting
    visibility = ScheduleVisibility.objects.first()
    if visibility is None:
        visibility = ScheduleVisibility.objects.create(is_live=False)

    # Fetch and order the conference days
    days = Day.objects.all().order_by('actual_date')
    
    # Prepare schedules per day
    schedules = {}
    for day in days:
        # Fetch both talks and events for the given day and event year
        schedules[day] = Schedule.objects.filter(
            conference_day=day
        ).filter(
            models.Q(talk__event_year=event_year) | models.Q(is_an_event=True)
        ).select_related('talk', 'talk__user').prefetch_related('talk__speakers').order_by('start_time')

    # Meta information for Open Graph and Twitter Cards
    meta_title = f"Schedule | PyCon Africa {year}"
    meta_description = f"Explore the schedule for PyCon Africa {year}, including keynotes, talks, tutorials, and more. Plan your conference experience with us."
    meta_og_image = "https://res.cloudinary.com/pycon-africa/image/upload/v1722977619/website_storage_location/media/schedule_og_image.png"  # Replace with a suitable image

    # Render the schedule page with days and their respective schedules
    return render(
        request,
        f'{year}/schedule/schedule.html',
        {
            'title': 'Schedule',
            'year': year,
            'days': days,
            'schedules': schedules,
            'is_schedule_live': visibility.is_live or request.user.is_superuser,
            'meta_title': meta_title,
            'meta_description': meta_description,
            'meta_og_image': meta_og_image,
        }
    )



class ScheduleDetailView(HitCountDetailView):
    model = Schedule
    context_object_name = 'schedule'
    slug_field = 'proposal_id'  # Ensure this field matches your model's field
    count_hit = True  # To count hits for hitcount feature
    paginate_by = 3

    def get_template_names(self):
        year = self.kwargs.get('year')
        return [f'{year}/schedule/schedule_details.html']

    def get_context_data(self, **kwargs):
        context = super(ScheduleDetailView, self).get_context_data(**kwargs)
        year = self.kwargs.get('year')
        event_year = get_object_or_404(EventYear, year=year)

        context.update({
            'talks': Proposal.objects.filter(status="A", event_year=event_year),
            'speakers': Profile.objects.filter(user__proposals__event_year=event_year).distinct(),
            'schedules': Schedule.objects.filter(talk__event_year=event_year),
            'event_year': event_year
        })
        return context


@login_required
@permission_required('conference_schedule.add_schedule', raise_exception=True)   
def create_talk_schedule(request, year):
    event_year = get_object_or_404(EventYear, year=year)

    if request.method == 'POST':
        form = TalkScheduleForm(request.POST)
        if form.is_valid():
            talk_schedule = form.save(commit=False)

            # Check if a talk was selected
            if talk_schedule.talk:
                talk_schedule.talk.event_year = event_year  # Only set event_year if a talk is selected
            
            talk_schedule.save()
            return redirect('conference_schedule:schedule', year=year)  # Update this with the correct app namespace
    else:
        form = TalkScheduleForm()

    return render(request, f'{year}/schedule/create_schedule.html', {'form': form, 'year': year})


 
@login_required
@permission_required('conference_schedule.add_schedule', raise_exception=True)
def create_new_talk_schedule(request, year):
    """
    View to create a new talk or event schedule for a specific event year.
    """
    # Get the event year based on the URL parameter
    event_year = get_object_or_404(EventYear, year=year)

    if request.method == 'POST':
        form = TalkScheduleForm(request.POST)
        
        if form.is_valid():
            # Get the form instance but don’t save it to the database just yet
            schedule_instance = form.save(commit=False)

            # Assign the event year to the talk if a talk is selected
            if schedule_instance.talk:
                schedule_instance.talk.event_year = event_year

            # Ensure start time is before end time
            if schedule_instance.start_time and schedule_instance.end_time:
                if schedule_instance.start_time >= schedule_instance.end_time:
                    form.add_error('start_time', 'Start time must be before end time.')
                    form.add_error('end_time', 'End time must be after start time.')
                    return render(request, f'{year}/schedule/create_schedule.html', {'form': form, 'year': year})
            
            # Save the schedule instance after additional checks
            schedule_instance.save()

            # Success message and redirection to the schedule overview page
            messages.success(request, 'The talk/event has been successfully scheduled.')
            return redirect('conference_schedule:schedule', year=year)
        else:
            # If form is not valid, render the form again with errors
            messages.error(request, 'There was an error with your submission. Please check the form and try again.')
    
    else:
        # Create an empty form for GET requests
        form = TalkScheduleForm()

    # Render the create schedule page with the form
    return render(request, f'{year}/schedule/new.html', {
        'form': form,
        'year': year,
        'event_year': event_year,
    })