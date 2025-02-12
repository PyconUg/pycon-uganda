from rest_framework import serializers

from conference_schedule.models import Schedule, Event, Day
from talks.models import Proposal


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('conference_day')


class TalkScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = all


class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        exclude = ('notes', 'talk_abstract', 'status')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = all
