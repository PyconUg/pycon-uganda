# Core Django imports.
from django.contrib import admin

# Blog application imports.
from .models import Fin_aid

class Fin_aidAdmin(admin.ModelAdmin):

    list_display = ('title', 'date_created')  
    ordering = ['-date_created', ]   

# Registers the Fin_aidmodel at the admin backend.
admin.site.register(Fin_aid, Fin_aidAdmin)

