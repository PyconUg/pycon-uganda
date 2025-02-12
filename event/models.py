from django.db import models
from django.utils import timezone
from home.models import EventYear

class Event(models.Model):
    name = models.CharField(max_length=255, help_text="The name of the event or activity.")
    description = models.TextField(help_text="Detailed description of the event.")
    date = models.DateField(default=timezone.now, help_text="Date of the event.")
    start_time = models.TimeField(default=timezone.now, help_text="Event start time.")
    end_time = models.TimeField(default=timezone.now, help_text="Event end time.")
    location = models.CharField(max_length=255, help_text="Location of the event.", blank=True, null=True)
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, help_text="The year this event belongs to.")
    is_featured = models.BooleanField(default=False, help_text="Indicates if this is a featured event.")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['date', 'start_time']

    def __str__(self):
        return f"{self.name} ({self.event_year.year})"
