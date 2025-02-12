import random
from django import template
from django.db.models import Q, Case, When, IntegerField, Exists, OuterRef
from registration.models import Profile
from talks.models import Proposal

register = template.Library()

@register.simple_tag
def get_speakers_for_homepage():
    queryset = Profile.objects.filter(
        Q(user__proposals__status='A', user__proposals__user_response='A') |
        Q(user__speaking_proposals__status='A', user__speaking_proposals__user_response='A')
    ).annotate(
        is_keynote_speaker=Exists(
            Proposal.objects.filter(
                user=OuterRef('user'),
                talk_type="Keynote Speaker",
                status='A',
                user_response='A'
            )
        ),
        sort_priority=Case(
            When(user__proposals__talk_type="Sponsored Talk", then=1),
            When(user__proposals__talk_type__in=["Short Talk", "Long Talk"], then=2),
            When(user__proposals__talk_type="Lightning Talk", then=3),
            default=4,
            output_field=IntegerField(),
        )
    ).order_by('sort_priority', 'user', 'date_created')
    
    # Remove duplicate users
    seen_users = set()
    unique_speakers = []
    for speaker in queryset:
        if speaker.user_id not in seen_users:
            seen_users.add(speaker.user_id)
            unique_speakers.append(speaker)

    # Separate keynote speakers
    keynote_speakers = [speaker for speaker in unique_speakers if speaker.is_keynote_speaker]
    
    # Separate and prioritize Sponsored Talk speakers
    sponsored_speakers = [speaker for speaker in unique_speakers if speaker.sort_priority == 1]

    # Get remaining speakers, excluding keynote and sponsored talk speakers
    other_speakers = [speaker for speaker in unique_speakers if not speaker.is_keynote_speaker and speaker.sort_priority != 1]

    # Shuffle and select remaining speakers to fill up the 4-speaker limit
    remaining_slots = max(0, 4 - len(sponsored_speakers))
    random.shuffle(other_speakers)
    selected_other_speakers = sponsored_speakers + other_speakers[:remaining_slots]

    # Ensure we only return 4 final speakers, prioritizing sponsored talk
    final_speakers = selected_other_speakers[:4]

    return {
        'keynote_speakers': keynote_speakers,
        'final_speakers': final_speakers,
    }
 

 