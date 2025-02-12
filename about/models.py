from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField 
from django.utils import timezone  
from markdownx.models import MarkdownxField 
from django.utils import timezone
from  embed_video.fields  import  EmbedVideoField   
from home.models import EventYear
from django_countries.fields import CountryField


class About(models.Model):
    about_title =  models.CharField(max_length=250, null=False, blank=False, help_text='About PyCon Africa') 
    about_tagline =  models.CharField(max_length=250, null=False, blank=True, help_text='Tagline for the year')
    about_image_one = models.ImageField(help_text="Upload your cover image or leave blank to use our default image",
                              upload_to='about_page') 
    section_one_title =  models.CharField(max_length=250, null=False, blank=True, default="WHAT IS | PYCON AFRICA?", help_text='About PyCon Africa') 
    section_one = MarkdownxField(default='', help_text = "[Supports Markdown] - About PyCon Africa.", null=False, blank=False
                             )
    section_two_title =  models.CharField(max_length=250, null=False, blank=True, default="THE | PROGRAM", help_text='About PyCon Africa') 
    section_two = MarkdownxField(default='', help_text = "[Supports Markdown] - About PyCon Africa.", null=False, blank=False
                             )
    section_three_title =  models.CharField(max_length=250, null=False, blank=True, default="THE | TEAM", help_text='About PyCon Africa') 
    section_three = MarkdownxField(default='', help_text = "[Supports Markdown] - About PyCon Africa.", null=False, blank=False
                             )
    section_four = MarkdownxField(default='', help_text = "[Supports Markdown] - More about PyCon Africa.", null=False, blank=True
                             )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=True, related_name='about_us', on_delete=models.CASCADE)
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="2024", related_name='abouts')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.about_title

    def get_absolute_url(self):
        return reverse("about_home")
 

 
class Venue(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False, help_text='Venue of PyCon Africa') 
    content = MarkdownxField(default='', help_text = "[Supports Markdown] - Content.", null=False, blank=False
                             )
    content_two = MarkdownxField(default='', help_text = "[Supports Markdown] - Content side two.", null=False, blank=False
                             )
    link_to_preview_video_url = EmbedVideoField(default="", blank=True, help_text='Link to Preview video on your Youtube or Google drive')
    google_map = models.CharField(default="",max_length=500, null=False, blank=False, help_text='Venue Google map ID')
    location = models.CharField(default="",max_length=250, null=False, blank=False, help_text='Location of Venue')
    location_address = models.CharField(default="",max_length=250, null=False, blank=False, help_text='Location of Venue')
    location_website = models.URLField(default="", blank=True, help_text="Venue's website if any") 
    image_one = models.URLField(default="", blank=False, help_text='Link to image')
    image_two = models.URLField(default="", blank=False, help_text='Link to image')
    first_day_of_event = models.DateTimeField(blank=True, null=True)
    last_day_of_event = models.DateTimeField(blank=True, null=True)
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="2024", related_name='venues')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('name',)
        verbose_name = 'venue'
        verbose_name_plural = 'venues'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("venue")
 
 
class Travel_Advice(models.Model): 
    title =  models.CharField(max_length=250, null=False, blank=False, help_text='Travel Advice PyCon Africa') 
    advice = MarkdownxField(default='', help_text = "[Supports Markdown] - Travel Advice PyCon Africa.", null=False, blank=False
                             )
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='travel_advice',default=User) 
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="2024", related_name='travel_advices')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("travel_advice")
 

class IOCGroup(models.Model):
    """
    Represents a group or category of IOC.
    """
    name = models.CharField(max_length=100)  # e.g., Moderating Team, Talks & Workshop Support
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="2024", related_name="ioc_groups")

    def __str__(self):
        return self.name
    
class IOCMember(models.Model):
    """
    Represents a core team member.
    """ 
    name = models.CharField(max_length=100)
    link = models.CharField(default="",blank=True, max_length=100)
    groups = models.ManyToManyField(IOCGroup, related_name="iocs",blank=True) 
    country = CountryField(default="GH",blank=False, blank_label='(select member contributing country)')
    country_2 = models.CharField(max_length=50, default="",blank=True, help_text='(enter member"s 2nd contributing country if any)')
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="2024", related_name='ioc_members')
    is_lead = models.BooleanField(default=False, help_text='Indicate if this member is a lead')

    def __str__(self):
        return self.name


class LOCGroup(models.Model):
    """
    Represents a group or category within the Local Organizing Committee.
    """
    name = models.CharField(max_length=100)  # e.g., Logistics Team, Venue Coordination
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="2024", related_name="loc_groups")

    def __str__(self):
        return self.name

class LOCMember(models.Model):
    """
    Represents an individual member of the Local Organizing Committee.
    """
    name = models.CharField(max_length=100)
    link = models.CharField(default="",blank=True, max_length=100)
    groups = models.ManyToManyField(LOCGroup, related_name="members", blank=True)
    country = CountryField(default="GH", blank=False, blank_label='(select member’s country)')
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="2024", related_name='loc_members')
    is_lead = models.BooleanField(default=False, help_text='Indicate if this member is a lead')

    def __str__(self):
        return self.name


class VolunteerGroup(models.Model):
    """
    Represents a group or category of volunteers.
    """
    name = models.CharField(max_length=100)  # e.g., Moderating Team, Talks & Workshop Support
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="2024", related_name="volunteer_groups")

    def __str__(self):
        return self.name

class Volunteer(models.Model):
    """
    Represents an individual volunteer, associated with one or more groups.
    """
    name = models.CharField(max_length=100)
    link = models.CharField(default="",blank=True, max_length=100)
    groups = models.ManyToManyField(VolunteerGroup, related_name="volunteers") 
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="2024", related_name="volunteers") 

    def __str__(self):
        return self.name