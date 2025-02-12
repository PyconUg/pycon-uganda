from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag
def navactive(request, urls):
    if request.path in ( reverse(url) for url in urls.split() ):
        return "active"
    return ""

@register.simple_tag
def time_of_day():
	import datetime, pytz
	from django.conf import settings
	cur_time = datetime.datetime.now(tz=pytz.timezone(str(settings.TIME_ZONE)))
	if cur_time.hour < 12:
		return 'Good Morning 🌅' 
	elif 12 <= cur_time.hour < 16:
		return 'Good Afternoon 🌞'
	else:
		return 'Good Evening 🌙'

 