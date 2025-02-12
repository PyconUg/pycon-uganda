from rest_framework import serializers

from .models import Proposal


class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        exclude = ('anything_else_you_want_to_tell_us', 'status')
