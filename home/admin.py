from  django.contrib import admin
from  .models import *
from django.conf import settings
from django.db import models   

# Register your models here. 
@admin.register(EventYear)
class EventYearAdmin(admin.ModelAdmin):
    list_display = ('year', 'home_info_shortened')
    search_fields = ('year', 'home_info')
    
    def home_info_shortened(self, obj):
        """
        Shorten the 'home_info' content for a cleaner display in the admin list view.
        """
        return (obj.home_info[:75] + '...') if len(obj.home_info) > 75 else obj.home_info
    home_info_shortened.short_description = 'Home Info'
