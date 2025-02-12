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


# Included by me (3rd Parties and more) 
from django.contrib.auth.models import User
from datetime import datetime  
from django.contrib.auth import authenticate, login, get_user_model 
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect 

# Coc application imports.
from .models import Coc   
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
 
from coc.mixins import EditOwnCocMixin, EditOwnLoginMixin
from .forms import CocForm  
from home.models import EventYear


 
def coc(request, year):
    event_year = get_object_or_404(EventYear, year=year)
    cocs = Coc.objects.filter(event_year=event_year).order_by('-date_created')
    template_name = f'{year}/coc/coc.html'  # Dynamically set based on the year
    return render(request, template_name, {'cocs': cocs, 'event_year': event_year})

def coc_edit(request, pk):
    coc = get_object_or_404(Coc, pk=pk)
    if request.method == "POST":
        form = CocForm(request.POST, instance=coc)
        if form.is_valid():
            coc = form.save(commit=False)
            coc.user = request.user
            coc.date_updated = timezone.now()
            coc.save()
            return redirect('coc:coc_home')
    else:
        form = CocForm(instance=coc)
    return render(request, '2022/coc/update_coc.html', {'form': form})

 
class CocView(EditOwnCocMixin, UpdateView):
    form_class = CocForm
    model = Coc
    template_name = "2022/coc/update_coc.html"
    success_url = reverse_lazy('coc:coc_home')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Coc'
        context['year'] = datetime.now().year
        try:
            context['coc'] = Coc()
        except Coc.DoesNotExist:
            context['coc'] = ''
        return context

def coc_update_view(UpdateView):
    obj = get_object_or_404(Coc, id=id)
    form = CocForm(UpdateView.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(UpdateView, "2022/coc/update_coc.html", context)

