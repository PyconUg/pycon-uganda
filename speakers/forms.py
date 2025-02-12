from django import forms

from registration.models import Profile

class SpeakerForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('name', 'biography')
