from django import template
from ..models import Schedule, Day, ScheduleVisibility
from home.models import EventYear
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
from django import template
from django.template.loader import get_template, TemplateDoesNotExist
from ..models import ScheduleVisibility, Schedule, Day
from django.db import models


register = template.Library()




@register.filter
def get_item(dictionary, key):
    """Custom template filter to get an item from a dictionary."""
    return dictionary.get(key)




@register.inclusion_tag('2024/schedule/schedule_home.html', takes_context=True)
def schedule_preview(context, year, limit=3):
    request = context['request']
    event_year = EventYear.objects.get(year=year)

    # Check visibility of the schedule
    visibility = ScheduleVisibility.objects.first()
    if visibility is None:
        visibility = ScheduleVisibility.objects.create(is_live=False)

    # If the schedule is not live and the user is not a superuser, return an empty schedule
    if not visibility.is_live and not request.user.is_superuser:
        return {
            'day_schedules': [],
            'year': year,
            'limit': limit,
            'is_schedule_live': visibility.is_live or request.user.is_superuser,
        }

    # Fetch all conference days and order by the actual date of the conference day
    days = Day.objects.all().order_by('actual_date')
    day_schedules = []

    for day in days:
        # Fetch both talks and events for each day, limited to the first `limit` items
        schedules = Schedule.objects.filter(
            conference_day=day
        ).filter(
            models.Q(talk__event_year=event_year) | models.Q(is_an_event=True)
        ).select_related('talk', 'talk__user').prefetch_related('talk__speakers').order_by('start_time')[:limit]
        
        # Add each day along with its schedules (even if there are no schedules)
        day_schedules.append({
            'day': day,
            'schedules': schedules
        })

    return {
        'day_schedules': day_schedules,
        'year': year,
        'limit': limit,
        'is_schedule_live': visibility.is_live,
    }