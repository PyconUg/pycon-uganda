# Core Django imports.
from django.contrib import admin

# Blog application imports.
from .models import Ticket 

class TicketAdmin(admin.ModelAdmin):

    list_display = ('ticket_title', 'date_created')  
    ordering = ['-date_created', ]   

# Registers the Ticket model at the admin backend.
admin.site.register(Ticket, TicketAdmin)

