from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event, EventYear

def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events_by_year', year=form.cleaned_data['event_year'].year)
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})

def events_by_year(request, year):
    events = Event.objects.filter(event_year__year=year)
    return render(request, 'events/events_by_year.html', {'events': events, 'year': year})
