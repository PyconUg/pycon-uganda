from django.contrib import admin
from django.utils.html import format_html
from .models import Sponsor
from sponsor_us.models import SponsorshipTier
from home.models import EventYear

class SponsorAdmin(admin.ModelAdmin):
    list_display = ("logo_preview", "name", "is_visible", "show_biography", "sponsor_type", "get_tier_display", "get_event_year_display")
    list_editable = ["is_visible", "show_biography"]
    list_filter = ["is_visible", "sponsor_type", "tier__name", "event_year__year"]
    search_fields = ['name', 'biography']
    # Removed autocomplete_fields to use dropdowns instead
    # autocomplete_fields = ['tier', 'event_year']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "tier":
            kwargs["queryset"] = SponsorshipTier.objects.all().order_by('display_order')
        if db_field.name == "event_year":
            kwargs["queryset"] = EventYear.objects.all().order_by('-year')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_tier_display(self, obj):
        return obj.tier.name if obj.tier else '-'
    get_tier_display.short_description = 'Tier'

    def get_event_year_display(self, obj):
        return obj.event_year.year if obj.event_year else '-'
    get_event_year_display.short_description = 'Event Year'

    # Method to show a preview of the logo
    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="width: 45px; height: 45px;" />', obj.logo.url)
        return "No Logo"
    logo_preview.short_description = 'Logo Preview'

admin.site.register(Sponsor, SponsorAdmin)


 