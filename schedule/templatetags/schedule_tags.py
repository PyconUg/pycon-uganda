from django import template
from conference_schedule.models import Schedule, Day, ScheduleVisibility
from home.models import EventYear
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
from django import template
from django.template.loader import get_template, TemplateDoesNotExist
from conference_schedule.models import ScheduleVisibility, Schedule, Day

register = template.Library()


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

    # Fetch all conference days
    days = Day.objects.all().order_by('conference_day')
    day_schedules = []

    for day in days:
        # Fetch both talks and events for each day, limited to the first `limit` items
        schedules = Schedule.objects.filter(
            conference_day=day
        ).select_related('talk', 'talk__user').prefetch_related('talk__speakers').order_by('start_time')[:limit]
        
        # Add each day along with its schedules (even if there are no schedules)
        day_schedules.append({
            'day': day,
            'schedules': schedules
        })

    # Attempt to get the correct template for the year, fallback to 'partials/schedule_home.html' if it doesn't exist
    template_path = f'{year}/schedule/schedule_home.html'
    try:
        get_template(template_path)
    except TemplateDoesNotExist:
        template_path = 'partials/schedule_home.html'

    return {
        'day_schedules': day_schedules,
        'year': year,
        'days': days,
        'limit': limit,
        'is_schedule_live': visibility.is_live,
        'template_path': template_path,
    }