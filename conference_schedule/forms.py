from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div, Row, Column
from django import forms
from .models import Schedule, Proposal 
from django.db import models






class TalkScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule  # Ensure this is from the correct app
        fields = '__all__'
        widgets = {
            'conference_day': forms.Select(attrs={'class': 'form-control'}),
            'talk': forms.Select(attrs={'class': 'form-control'}),
            'event': forms.TextInput(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'step': '60'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'step': '60'}),
            'day_session': forms.Select(attrs={'class': 'form-control'}),
            'allocated_room': forms.Select(attrs={'class': 'form-control'}),
            'event_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter event URL'}),
            'external_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter external URL'}),
        }

    def __init__(self, *args, **kwargs):
        super(TalkScheduleForm, self).__init__(*args, **kwargs)

        # Initialize Crispy Forms helper
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column(Field('conference_day'), css_class='form-group col-md-6 mb-0'),
                Column(Field('talk'), css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column(Field('event'), css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column(Field('start_time'), css_class='form-group col-md-6 mb-0'),
                Column(Field('end_time'), css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column(Field('day_session'), css_class='form-group col-md-6 mb-0'),
                Column(Field('allocated_room'), css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column(Field('event_url'), css_class='form-group col-md-6 mb-0'),
                Column(Field('external_url'), css_class='form-group col-md-6 mb-0'),
            ),
            Submit('submit', 'Save Schedule', css_class='btn btn-primary')
        )

        # Fetch the instance being edited
        instance = kwargs.get('instance')
        
        # Fetch talks already scheduled
        scheduled_talks = Schedule.objects.filter(talk__isnull=False).values_list('talk_id', flat=True)

        # If we're editing a schedule, allow the current talk to be in the dropdown
        if instance and instance.talk:
            current_talk_id = instance.talk.proposal_id  # Assuming 'proposal_id' is the primary key
            # Exclude all scheduled talks except the current one
            available_talks = Proposal.objects.filter(
                status='A', user_response='A'
            ).exclude(pk__in=scheduled_talks).union(
                Proposal.objects.filter(pk=current_talk_id)
            )
        else:
            # Exclude all already scheduled talks
            available_talks = Proposal.objects.filter(
                status='A', user_response='A'
            ).exclude(pk__in=scheduled_talks)

        # Add available talks to the dropdown
        talk_choices = [(talk.pk, talk.title) for talk in available_talks]
        self.fields['talk'].choices = [('', 'Select a talk')] + talk_choices

        # Set placeholders and help texts dynamically
        self.fields['event'].widget.attrs.update({'placeholder': 'Enter event name'})
        self.fields['talk'].widget.attrs.update({'placeholder': 'Select a talk'})





        