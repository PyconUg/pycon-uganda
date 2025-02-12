# Core Django imports.
from django.contrib import admin

# About application imports.
from .models import (
    About,
    Venue,
    Travel_Advice,
    IOCGroup,
    IOCMember,
    LOCGroup,
    LOCMember,
    VolunteerGroup,
    Volunteer,
)

# If you plan to use adminsortable2 (optional)
# from adminsortable2.admin import SortableAdminMixin

# AboutAdmin
class AboutAdmin(admin.ModelAdmin):
    list_display = ('about_title', 'user', 'event_year', 'date_created')
    ordering = ['-date_created']
    exclude = ('user',)  # Exclude the user field from the admin form

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created (and not modified)
            obj.user = request.user  # Set the user to the current user
        super().save_model(request, obj, form, change)

# VenueAdmin
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_year', 'date_created')
    ordering = ['-date_created']
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

# TravelAdviceAdmin
class TravelAdviceAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'event_year', 'date_created')
    ordering = ['-date_created']
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

# IOCGroupAdmin
class IOCGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_year')
    list_filter = ('event_year',)
    search_fields = ('name',)

# IOCMemberAdmin
@admin.register(IOCMember)
class IOCMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_year', 'is_lead')
    list_filter = ('event_year', 'is_lead')
    search_fields = ('name',)
    list_editable = ('is_lead',)
    filter_horizontal = ('groups',)  # To make many-to-many field manageable

# LOCGroupAdmin
class LOCGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_year')
    list_filter = ('event_year',)
    search_fields = ('name',)

# LOCMemberAdmin
@admin.register(LOCMember)
class LOCMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_year', 'is_lead')
    list_filter = ('event_year', 'is_lead')
    search_fields = ('name',)
    list_editable = ('is_lead',)
    filter_horizontal = ('groups',)  # To make many-to-many field manageable

# VolunteerGroupAdmin
class VolunteerGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_year')
    list_filter = ('event_year',)
    search_fields = ('name',)

# VolunteerAdmin
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_year')
    list_filter = ('event_year', 'groups')
    search_fields = ('name',)
    filter_horizontal = ('groups',)

# Register your models and admin classes
admin.site.register(About, AboutAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Travel_Advice, TravelAdviceAdmin)
admin.site.register(IOCGroup, IOCGroupAdmin)
admin.site.register(LOCGroup, LOCGroupAdmin)
admin.site.register(VolunteerGroup, VolunteerGroupAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
