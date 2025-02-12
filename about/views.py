#home views 
import operator

# Core Django imports.
from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib import messages
from django.db.models import Q 
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic import (
    DetailView,
    ListView,
)
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from functools import reduce

# About application imports.
from .models import *
from .models import About, Venue
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Included by me (3rd Parties and more) 
from django.contrib.auth.models import User
from datetime import datetime 
from .forms import *

from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect 

from about.mixins import EditOwnAboutMixin, EditOwnLoginMixin


# Create your views here. 
def redirect_to_current_year_about(request):
    current_year = timezone.now().year
    return redirect('abouts', year=current_year)

def current_event_year(year=None):
    if year is None:
        year = timezone.now().year
    return EventYear.objects.filter(year=year).first()

def about(request, year):
    event_year = get_object_or_404(EventYear, year=year)
    abouts = About.objects.filter(event_year=event_year).order_by('-date_created')
    template_name = f'{year}/about/about.html'
    return render(request, template_name, {'abouts': abouts, 'event_year': event_year})

def about_edit(request, pk, year):
    about = get_object_or_404(About, pk=pk)
    event_year = get_object_or_404(EventYear, year=year)
    if request.method == "POST":
        form = AboutForm(request.POST, instance=about)
        if form.is_valid():
            about.save()
            return redirect('about:about_home', year=event_year.year)
    else:
        form = AboutForm(instance=about)
    template_name = f'{year}/about/update_about.html'
    return render(request, template_name, {'form': form, 'event_year': event_year})

class AboutView(EditOwnAboutMixin, UpdateView):
    form_class = AboutForm
    model = About

    def get_template_names(self):
        year = self.kwargs.get('year')
        return [f"{year}/about/update_about.html"]

    def get_success_url(self):
        year = self.kwargs.get('year')
        return reverse_lazy('about:about_home', kwargs={'year': year})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = self.kwargs.get('year')
        context['year'] = year
        return context

def venue(request, year):
    event_year = get_object_or_404(EventYear, year=year)
    venues = Venue.objects.filter(event_year=event_year).order_by('-date_created')
    template_name = f'{year}/about/venue.html'
    return render(request, template_name, {'venues': venues, 'event_year': event_year})

def teams_view(request, year):
    event_year = get_object_or_404(EventYear, year=year)

    # International Organizing Committee
    ioc_groups = IOCGroup.objects.filter(event_year=event_year)

    # Prepare IOC members per group with leads and non-leads
    ioc_groups_with_members = []
    for group in ioc_groups:
        leads = group.iocs.filter(event_year=event_year, is_lead=True).order_by('name')
        non_leads = group.iocs.filter(event_year=event_year, is_lead=False).order_by('name')
        ioc_groups_with_members.append({
            'group': group,
            'leads': leads,
            'non_leads': non_leads,
        })

    # Fetch IOC members not in any group
    ioc_ungrouped_members = IOCMember.objects.filter(
        event_year=event_year,
        groups__isnull=True
    ).order_by('name')

    if ioc_ungrouped_members.exists():
        # Separate leads and non-leads
        ungrouped_leads = ioc_ungrouped_members.filter(is_lead=True)
        ungrouped_non_leads = ioc_ungrouped_members.filter(is_lead=False)

        # Create a pseudo-group for ungrouped members
        pseudo_group = IOCGroup(name='Other Committee Members')

        ioc_groups_with_members.append({
            'group': pseudo_group,
            'leads': ungrouped_leads,
            'non_leads': ungrouped_non_leads,
        })

    # Local Organizing Committee
    loc_groups = LOCGroup.objects.filter(event_year=event_year)

    # Prepare LOC members per group with leads and non-leads
    loc_groups_with_members = []
    for group in loc_groups:
        leads = group.members.filter(event_year=event_year, is_lead=True).order_by('name')
        non_leads = group.members.filter(event_year=event_year, is_lead=False).order_by('name')
        loc_groups_with_members.append({
            'group': group,
            'leads': leads,
            'non_leads': non_leads,
        })

    # Fetch LOC members not in any group (if applicable)
    loc_ungrouped_members = LOCMember.objects.filter(
        event_year=event_year,
        groups__isnull=True
    ).order_by('name')

    if loc_ungrouped_members.exists():
        # Separate leads and non-leads
        loc_ungrouped_leads = loc_ungrouped_members.filter(is_lead=True)
        loc_ungrouped_non_leads = loc_ungrouped_members.filter(is_lead=False)

        # Create a pseudo-group for ungrouped members
        pseudo_group = LOCGroup(name='Other Committee Members')

        loc_groups_with_members.append({
            'group': pseudo_group,
            'leads': loc_ungrouped_leads,
            'non_leads': loc_ungrouped_non_leads,
        })

    # Volunteers
    volunteer_groups = VolunteerGroup.objects.filter(event_year=event_year)
    volunteers = Volunteer.objects.filter(event_year=event_year).order_by('name')

    context = {
        'event_year': event_year,
        'ioc_groups_with_members': ioc_groups_with_members,
        'loc_groups_with_members': loc_groups_with_members,
        'volunteer_groups': volunteer_groups,
        'volunteers': volunteers,
    }

    template_name = f'{year}/about/teams.html'

    return render(request, template_name, context)






def travel_advice(request, year):
    event_year = get_object_or_404(EventYear, year=year)
    travel_advices = Travel_Advice.objects.filter(event_year=event_year).order_by('-date_created')
    template_name = f'{year}/about/travel.html'
    return render(request, template_name, {'travel_advices': travel_advices, 'event_year': event_year})
 

 #2020 

 
def hopin(request):
    context = {"about": "active"}
    template = '2020/hopin.html'
    return render(request, template, context)