from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'start_time', 'end_time', 'location', 'event_year', 'is_featured']
