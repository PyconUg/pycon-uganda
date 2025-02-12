from django.db import models
from django.utils import timezone
from registration.models import Profile
from talks.models import Proposal
from event.models import *
from home.models import EventYear
from django.utils.dateparse import parse_date
from django.core.exceptions import ValidationError
from event.models import Event
from django.conf import settings
import datetime



class Day(models.Model):
    conference_day = models.CharField(max_length=30, unique=True, help_text="The name of the conference day (e.g., Day 1, Day 2).") 
    actual_date = models.DateField(help_text="The actual date of the conference day.", default=datetime.date(2024, 9, 9))

    class Meta:
        verbose_name = "Conference Day"
        verbose_name_plural = "Conference Days"
        ordering = ['actual_date']

    def __str__(self):
        return self.actual_date.strftime('%Y-%m-%d')


class Room(models.Model):
    room_name = models.CharField(max_length=50, unique=True, null=True, blank=True, help_text="The name or number of the conference room.")

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ['room_name']

    def __str__(self):
        return self.room_name


class Schedule(models.Model):
    DAY_SESSIONS = (
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening'),
    )

    conference_day = models.ForeignKey(Day, on_delete=models.CASCADE)
    talk = models.ForeignKey(Proposal, on_delete=models.CASCADE, blank=True, null=True, help_text="Select a Talk if it's a Speaker giving a talk")
    event = models.CharField(max_length=255, default="", blank=True, help_text="The name of the event or activity.")
    event_description = models.TextField(blank=True, help_text="A short description of the event.") 
    is_an_event = models.BooleanField(default=False, help_text="Indicate if this is an event instead of a talk.")
    fa_icon = models.CharField(max_length=100, default='', blank=True)
    event_url = models.CharField(max_length=250, default="", blank=True, help_text='URL to the event')
    external_url = models.CharField(max_length=250, default="", blank=True, help_text='External link to the event')

    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    day_session = models.CharField(max_length=10, choices=DAY_SESSIONS, default='', blank=True)
    allocated_room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    rowspan = models.CharField(max_length=10, default='', blank=True, help_text="Use to determine how this talk fits in its time allocation")
    concurrent_talk = models.BooleanField(default=False)
    is_a_keynote_speaker = models.BooleanField(default=False)
    is_a_panel = models.BooleanField(default=False)

    class Meta:
        managed = True
        verbose_name_plural = "Talk Schedules"
        indexes = [
            models.Index(fields=['start_time', 'end_time']),
        ]

        permissions = [
            ("can_manage_schedule", "Can manage schedules"),
        ]

    def __str__(self):
        if self.is_an_event:
            return f"{self.event} in {self.allocated_room}" if self.allocated_room else f"{self.event}"
        
        if self.talk:
            if self.talk.speakers.exists():
                # Safely retrieve either the profile name or fall back to "PyCon Africa"
                speakers_names = ', '.join([getattr(speaker.user_profile, 'name', 'PyCon Africa') for speaker in self.talk.speakers.all()])
                return f"{self.talk.title} by {speakers_names}"
            else:
                return self.talk.title

        return "No event or talk assigned"

    def clean(self):
        super().clean()
        if not self.talk and not self.event:
            raise ValidationError('Either a talk or an event must be selected.')
        if self.talk and self.event:
            raise ValidationError('You cannot have both a talk and an event in the same schedule entry.')
        if self.is_an_event and not self.event:
            raise ValidationError('You must provide an event name if this is an event.')
        if self.is_an_event and self.talk and self.talk.speakers.exists():
            raise ValidationError('Speakers cannot be assigned to events.')
        if self.start_time and self.end_time and self.start_time >= self.end_time:
            raise ValidationError('The start time must be before the end time.')

    def save(self, *args, **kwargs):
        self.clean()
        conference_date = self.conference_day.actual_date
        if conference_date and self.start_time and self.end_time:
            start_datetime = timezone.datetime.combine(conference_date, self.start_time)
            end_datetime = timezone.datetime.combine(conference_date, self.end_time)
            if timezone.is_naive(start_datetime):
                start_datetime = timezone.make_aware(start_datetime)
            if timezone.is_naive(end_datetime):
                end_datetime = timezone.make_aware(end_datetime)
            self.start_time = start_datetime
            self.end_time = end_datetime
        super().save(*args, **kwargs)

        

class ScheduleVisibility(models.Model):
    is_live = models.BooleanField(default=False, help_text="Indicates if the schedule is live and visible to all users.")

    class Meta:
        verbose_name = "Schedule Visibility"
        verbose_name_plural = "Schedule Visibility"

    def __str__(self):
        return "Live" if self.is_live else "Not Live"
