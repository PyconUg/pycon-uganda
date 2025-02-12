# Core Django imports.
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.admin.options import TabularInline, StackedInline

# Blog application imports.
from .models import Event   
from registration.admin import SpeakerInline
#from sponsors.admin import SponsorInline
 


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location' )  
    ordering = ['name', '-date_created', ]   
    #inlines = [SponsorInline]
        

# Registers the Event model at the admin backend.
admin.site.register(Event, EventAdmin)

