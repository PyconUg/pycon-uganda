# Core Django imports.
from django.contrib import admin

# Blog application imports.
from .models import Health_Safety_Guideline

class Health_Safety_GuidelineAdmin(admin.ModelAdmin):

    list_display = ('title', 'date_created')  
    ordering = ['-date_created', ]   

# Registers the Health_Safety_Guidelinemodel at the admin backend.
admin.site.register(Health_Safety_Guideline, Health_Safety_GuidelineAdmin)

