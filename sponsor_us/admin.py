# Core Django imports.
from django.contrib import admin
from .models import *
from markdownx.admin import MarkdownxModelAdmin  


class SponsorshipBenefitInline(admin.StackedInline):
    model = SponsorshipBenefit
    extra = 1

class AdditionalResourceInline(admin.StackedInline):
    model = AdditionalResource
    extra = 1


@admin.register(SponsorUsPage)
class SponsorUsPageAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'user', 'event_year', 'date_created', 'date_updated') 
    exclude = ('user',)  # Exclude the user field from the admin form 
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created (and not modified)
            obj.user = request.user  # Set the user to the current user
        super().save_model(request, obj, form, change)

@admin.register(SponsorshipTier)
class SponsorshipTierAdmin(MarkdownxModelAdmin):
    list_display = ('name', 'show_in_grid', 'display_order', 'amount', 'colour', 'hex', 'date_created', 'date_updated')
    list_editable = ('show_in_grid',)        
    inlines = [SponsorshipBenefitInline, AdditionalResourceInline]
    search_fields = ['name',]   
    exclude = ('user',)  # Exclude the user field from the admin form 
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created (and not modified)
            obj.user = request.user  # Set the user to the current user
        super().save_model(request, obj, form, change)

# You may or may not need to use MarkdownxModelAdmin for SponsorshipBenefit
# and AdditionalResource if they do not contain MarkdownxFields.
class SponsorshipBenefitAdmin(admin.ModelAdmin):
    list_display = ('tier_display', 'description_short')

    def tier_display(self, obj):
        return str(obj.tier)
    tier_display.short_description = 'Tier'

    def description_short(self, obj):
        return (obj.description[:75] + '...') if len(obj.description) > 75 else obj.description
    description_short.short_description = 'Description'

admin.site.register(SponsorshipBenefit, SponsorshipBenefitAdmin)

@admin.register(AdditionalResource)
class AdditionalResourceAdmin(admin.ModelAdmin):
    list_display = ('sponsorship_tier', 'package')



