# Core Django imports.
from django.contrib import admin

# Blog application imports.
from .models import PrivacyPolicy

class PrivacyPolicyAdmin(admin.ModelAdmin):

    list_display = ('title', 'date_created')  
    ordering = ['-date_created', ]   

# Registers the PrivacyPolicymodel at the admin backend.
admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)

