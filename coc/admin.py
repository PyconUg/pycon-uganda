# Core Django imports.
from django.contrib import admin

# Blog application imports.
from .models import Coc

class CocAdmin(admin.ModelAdmin):

    list_display = ('title', 'user', 'event_year', 'date_created')  
    ordering = ['-date_created', ]   

    exclude = ('user',)  # Exclude the user field from the admin form 
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created (and not modified)
            obj.user = request.user  # Set the user to the current user
        super().save_model(request, obj, form, change)

# Registers the Cocmodel at the admin backend.
admin.site.register(Coc, CocAdmin)

