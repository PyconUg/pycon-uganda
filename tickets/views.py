#home views   
from django.template import RequestContext  
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

# Ticket application imports.
from .models import Ticket   
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Included by me (3rd Parties and more) 
from django.contrib.auth.models import User
from datetime import datetime 
from .forms import TicketForm

from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect  
from home.models import EventYear
from tickets.mixins import EditOwnTicketMixin, EditOwnLoginMixin
 
# Create your views here. 

def ticket(request, year):
    event_year = get_object_or_404(EventYear, year=year)
    tickets = Ticket.objects.filter(event_year=event_year).order_by('-date_created')
    if tickets.exists():
        first_ticket = tickets.first()
        meta_og_image = first_ticket.image_url
    else:
        meta_og_image = 'default_image_url'

    context = {
        'tickets': tickets,
        'event_year': event_year,
        'meta_title': f"Tickets for PyCon Africa {year}",
        'meta_description': "Join us at PyCon Africa! Get your tickets for this year's event and don't miss out.",
        'meta_author': "PyCon Africa",
        'meta_og_image': meta_og_image,
    }
    template_name = f'{year}/tickets/tickets.html'  # Dynamically set based on the year
    return render(request, template_name, context)
    


def ticket_edit(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.date_updated = timezone.now()
            ticket.save()
            return redirect('ticket:ticket_home')
    else:
        form = TicketForm(instance=ticket)
    return render(request, '2022/ticket/update_ticket.html', {'form': form})

 
class TicketView(EditOwnTicketMixin, UpdateView):
    form_class = TicketForm
    model = Ticket
    template_name = "2022/ticket/update_ticket.html"
    success_url = reverse_lazy('ticket:ticket_home')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Ticket'
        context['year'] = datetime.now().year
        try:
            context['ticket'] = Ticket()
        except Ticket.DoesNotExist:
            context['ticket'] = ''
        return context

def ticket_update_view(UpdateView):
    obj = get_object_or_404(Ticket, id=id)
    form = TicketForm(UpdateView.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(UpdateView, "2022/ticket/update_ticket.html", context)




def register(request):
    context = {}
    template = '2022/ticket/register.html'
    return render(request, template, context)