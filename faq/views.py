#home views 
import operator

# Core Django imports.
from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib import messages
from django.db.models import Q 
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic import (
    DetailView,
    ListView,
)
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from functools import reduce
from home.models import EventYear
# FrequentlyAskedQuestion application imports.
from .models import FrequentlyAskedQuestion 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
 
 
def faq(request, year):
    # Ensure the event year exists and is valid
    event_year = get_object_or_404(EventYear, year=year)
    # Filter FAQs based on the event year
    faqs = FrequentlyAskedQuestion.objects.filter(event_year=event_year).order_by('-date_created')
    # Render the template with FAQs specific to the given year
    return render(request, f'{year}/faq/faq.html', {'faqs': faqs})