from django.contrib import admin
from conference_schedule.models import Schedule, Room, Day, ScheduleVisibility   
from conference_schedule.forms import TalkScheduleForm  
 
from  .models import Schedule   
class TalkScheduleAdmin(admin.ModelAdmin):
    form = TalkScheduleForm  # Use the custom form

    list_display = ('get_talk_or_event', 'allocated_room', 'conference_day', 'concurrent_talk', 'start_time', 'end_time', 'is_an_event', 'is_a_keynote_speaker', 'is_a_panel')
    list_editable = ['allocated_room', 'conference_day', 'start_time', 'end_time', 'is_an_event', 'concurrent_talk', 'is_a_keynote_speaker', 'is_a_panel']
    
    # Filters to enhance usability
    list_filter = ['conference_day', 'allocated_room', 'is_a_keynote_speaker', 'is_a_panel', 'concurrent_talk']
    
    # Adding search capabilities
    search_fields = ['talk__title', 'event']

    # Ensure ordering is by conference day and start time
    ordering = ['conference_day__actual_date', 'start_time']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('talk', 'allocated_room', 'conference_day').order_by('conference_day__actual_date', 'start_time')

    # Custom admin actions
    actions = ['mark_as_keynote', 'mark_as_panel']

    def mark_as_keynote(self, request, queryset):
        queryset.update(is_a_keynote_speaker=True)
        self.message_user(request, "Selected talks are now marked as keynote speakers.")

    def mark_as_panel(self, request, queryset):
        queryset.update(is_a_panel=True)
        self.message_user(request, "Selected talks are now marked as panels.")

    mark_as_keynote.short_description = "Mark selected talks as keynote speakers"
    mark_as_panel.short_description = "Mark selected talks as panels"

    # Custom method to display either the talk or event in list_display
    def get_talk_or_event(self, obj):
        if obj.is_an_event:
            return obj.event
        elif obj.talk:
            return obj.talk.title
        return "N/A"
    
    get_talk_or_event.short_description = 'Talk/Event'


# Register the Schedule model with the updated admin
admin.site.register(Schedule, TalkScheduleAdmin)

admin.site.register(Room)
admin.site.register(Day)


@admin.register(ScheduleVisibility)
class ScheduleVisibilityAdmin(admin.ModelAdmin):
    list_display = ('is_live',)
    actions = ['make_live', 'make_not_live']

    def make_live(self, request, queryset):
        queryset.update(is_live=True)
        self.message_user(request, "The schedule is now live and visible to all users.")

    def make_not_live(self, request, queryset):
        queryset.update(is_live=False)
        self.message_user(request, "The schedule is now hidden from all users except superusers.")

    make_live.short_description = "Make schedule live"
    make_not_live.short_description = "Hide schedule from users"
