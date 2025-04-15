from __future__ import absolute_import
from django.shortcuts import render, reverse
from .models import *
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect 




# Create your views here. 
def sponsor_us(request, year):
    # Fetch the EventYear instance or raise a 404 error if not found
    event_year = get_object_or_404(EventYear, year=year)

    # Fetch the SponsorUsPage for the specified year or raise a 404 error if not found
    sponsor_us_page = get_object_or_404(SponsorUsPage, event_year=event_year)

    # Fetch all SponsorshipTier instances for the specified year, ordered by 'display_order'
    sponsorship_tiers = SponsorshipTier.objects.filter(user=sponsor_us_page.user).order_by('display_order')

    # Building the context
    context = {
        'event_year': event_year,
        'sponsor_us_page': sponsor_us_page,
        'sponsorship_tiers': sponsorship_tiers,
    }

    # Dynamically building the template path based on the event year
    template_name = f'{year}/sponsor-us/sponsor-us.html'

    return render(request, template_name, context)

def thank_you(request):
    context = {}
    template = '2022/sponsor-us/thankyou.html'
    return render(request, template, context)