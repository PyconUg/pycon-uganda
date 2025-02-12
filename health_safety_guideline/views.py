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

# Included by me (3rd Parties and more) 
from django.contrib.auth.models import User
from datetime import datetime  
from django.contrib.auth import authenticate, login, get_user_model 
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect 

# Health_Safety_Guideline application imports.
from .models import Health_Safety_Guideline   
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
 
from health_safety_guideline.mixins import EditOwnHealth_Safety_GuidelineMixin, EditOwnLoginMixin
from .forms import Health_Safety_GuidelineForm
 
 
def health_safety_guideline(request, year):
    # Ensure the event year exists and is valid
    event_year = get_object_or_404(EventYear, year=year)
    # Filter Health and Safety Guidelines based on the event year
    health_safety_guidelines = Health_Safety_Guideline.objects.filter(event_year=event_year).order_by('-date_created')
    # Render the template with Health and Safety Guidelines specific to the given year
    return render(request, f'{year}/health_safety_guidelines/health_safety_guidelines.html', {'health_safety_guidelines': health_safety_guidelines})

def health_safety_guideline_edit(request, pk):
    health_safety_guideline = get_object_or_404(Health_Safety_Guideline, pk=pk)
    if request.method == "POST":
        form = Health_Safety_GuidelineForm(request.POST, instance=health_safety_guideline)
        if form.is_valid():
            health_safety_guideline = form.save(commit=False)
            health_safety_guideline.user = request.user
            health_safety_guideline.date_updated = timezone.now()
            health_safety_guideline.save()
            return redirect('health_safety_guideline:health_safety_guideline_home')
    else:
        form = Health_Safety_GuidelineForm(instance=health_safety_guideline)
    return render(request, '2024/health_safety_guideline/update_health_safety_guideline.html', {'form': form})

 
class Health_Safety_GuidelineView(EditOwnHealth_Safety_GuidelineMixin, UpdateView):
    form_class = Health_Safety_GuidelineForm
    model = Health_Safety_Guideline
    template_name = "2024/health_safety_guideline/update_health_safety_guideline.html"
    success_url = reverse_lazy('health_safety_guideline:health_safety_guideline_home')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Health_Safety_Guideline'
        context['year'] = datetime.now().year
        try:
            context['health_safety_guideline'] = Health_Safety_Guideline()
        except Health_Safety_Guideline.DoesNotExist:
            context['health_safety_guideline'] = ''
        return context

def health_safety_guideline_update_view(UpdateView):
    obj = get_object_or_404(Health_Safety_Guideline, id=id)
    form = Health_Safety_GuidelineForm(UpdateView.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(UpdateView, "2024/health_safety_guideline/update_health_safety_guideline.html", context)

