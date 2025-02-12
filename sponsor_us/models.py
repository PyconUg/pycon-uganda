from django.db import models 
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField 
from django.utils import timezone  
from home.models import EventYear


class SponsorUsPage(models.Model):
    title = models.CharField(max_length=250, help_text='Support PyCon Africa')
    why_sponsor_us = MarkdownxField(help_text="[Supports Markdown] - Support PyCon Africa.")
    special_sponsorship = MarkdownxField(help_text="[Supports Markdown] - Special sponsorship package.")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supportus_pages')
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, related_name='supportus_pages')
    prospectus_link = models.URLField(blank=True, help_text="Link to the sponsorship prospectus.")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class SponsorshipBenefit(models.Model):
    description = MarkdownxField(default='', help_text = "[Supports Markdown] - Full Benefit in .md", null=False, blank=False)
    tier = models.ForeignKey('SponsorshipTier', on_delete=models.CASCADE, related_name='benefits')  
    
    def __str__(self):
        return self.description


class SponsorshipTier(models.Model):
    name = models.CharField(max_length=100, help_text="Sponsorship Tier name. eg, Gold, Silver")
    amount = models.IntegerField(help_text="Sponsorship Tier Amount eg, 1000.00")  
    colour = models.CharField(max_length=25, default="primary", help_text="Colour for tier eg, yellow, gray, primary etc")
    hex = models.CharField(max_length=25, default="#000", help_text="Hex colour for tier eg, #cd7f32")
    details = MarkdownxField(help_text="[Supports Markdown] - Detailed description of the tier.")
    display_order = models.IntegerField(default=0, help_text="Order in which the tier should be displayed.")
    show_in_grid = models.BooleanField(default=False, help_text="Tick this if the sponsors in this tier should be displayed in a grid layout.")
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, related_name='sponsorship_tiers', null=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sponsorship_tier_users')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} Tier"
    
class AdditionalResource(models.Model):
    sponsorship_tier = models.ForeignKey(SponsorshipTier, on_delete=models.CASCADE, related_name='additional_resources') 
    package = models.TextField(blank=True)

    def __str__(self):
        return str(self.sponsorship_tier) 