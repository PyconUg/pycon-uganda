from django import template
from ..models import Sponsor
from django.template.loader import render_to_string


register = template.Library()

@register.simple_tag(takes_context=True)
def show_sponsor(context):
    sponsor = Sponsor.objects.filter(is_visible=True)
    latest_year = sponsor.first().event_year.year if sponsor.exists() else 2024
    template_name = f'{latest_year}/sponsors/footer_sponsors.html'
    return render_to_string(template_name, {'sponsor': sponsor, 'event_year': latest_year}, request=context['request'])

@register.simple_tag(takes_context=True)
def show_home_sponsor(context):
    sponsor_h_home = Sponsor.objects.filter(is_visible=True, tier__name="HEADLINE SPONSOR")
    sponsor_p_home = Sponsor.objects.filter(is_visible=True, tier__name="PLATINUM")
    sponsor_d_home = Sponsor.objects.filter(is_visible=True, tier__name="DIAMOND")
    sponsor_g_home = Sponsor.objects.filter(is_visible=True, tier__name="GOLD")
    latest_year = sponsor_h_home.first().event_year.year if sponsor_h_home.exists() else 2024
    template_name = f'{latest_year}/sponsors/home_sponsors.html'
    return render_to_string(template_name, {
        'sponsor_h_home': sponsor_h_home,
        'sponsor_p_home': sponsor_p_home,
        'sponsor_d_home': sponsor_d_home,
        'sponsor_g_home': sponsor_g_home,
        'event_year': latest_year
    }, request=context['request'])