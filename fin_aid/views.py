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

# Fin_aid application imports.
from .models import Fin_aid   
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from home.models import EventYear
 
from django.contrib.auth.mixins import PermissionRequiredMixin
from fin_aid.mixins import EditOwnFin_aidMixin, EditOwnLoginMixin
from .forms import Fin_aidForm


def fin_aid(request, year):
    event_year = get_object_or_404(EventYear, year=year)
    fin_aids = Fin_aid.objects.filter(event_year=event_year).order_by('-date_created')
    for fin_aid in fin_aids:
        fin_aid.is_open = fin_aid.is_form_open()
        fin_aid.is_closed = fin_aid.is_form_closed()
        fin_aid.not_open_yet = fin_aid.is_form_not_open_yet()
        fin_aid.form_status_message = fin_aid.get_form_status_message()
    return render(request, f'{year}/fin_aid/fin_aid.html', {'fin_aids': fin_aids, 'year': year})

@login_required
def fin_aid_edit(request, year, pk):
    fin_aid = get_object_or_404(Fin_aid, pk=pk)
    if not request.user.has_perm('fin_aid.can_edit_fin_aid'):
        return redirect('fin_aid', year=year)
    if request.method == "POST":
        form = Fin_aidForm(request.POST, instance=fin_aid)
        if form.is_valid():
            fin_aid = form.save(commit=False)
            fin_aid.user = request.user
            fin_aid.date_updated = timezone.now()
            fin_aid.save()
            return redirect('fin_aid', year=year)
    else:
        form = Fin_aidForm(instance=fin_aid)
    return render(request, f'{year}/fin_aid/update_fin_aid.html', {'form': form, 'year': year})

class Fin_aidView(PermissionRequiredMixin, UpdateView):
    form_class = Fin_aidForm
    model = Fin_aid
    template_name = "fin_aid/update_fin_aid.html"
    permission_required = 'fin_aid.can_edit_fin_aid'

    def get_success_url(self):
        return reverse_lazy('fin_aid', kwargs={'year': self.object.event_year.year})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Fin_aid'
        context['year'] = timezone.now().year
        context['fin_aid'] = self.object
        context['is_open'] = self.object.is_form_open()
        context['is_closed'] = self.object.is_form_closed()
        context['not_open_yet'] = self.object.is_form_not_open_yet()
        context['form_status_message'] = self.object.get_form_status_message()
        return context

@login_required
def fin_aid_update_view(request, year, id):
    obj = get_object_or_404(Fin_aid, id=id)
    if not request.user.has_perm('fin_aid.can_edit_fin_aid'):
        return redirect('fin_aid', year=year)
    if request.method == "POST":
        form = Fin_aidForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('fin_aid', year=year)
    else:
        form = Fin_aidForm(instance=obj)
    context = {
        'form': form,
        'is_open': obj.is_form_open(),
        'is_closed': obj.is_form_closed(),
        'not_open_yet': obj.is_form_not_open_yet(),
        'form_status_message': obj.get_form_status_message(),
        'year': year
    }
    return render(request, f'{year}/fin_aid/update_fin_aid.html', context)