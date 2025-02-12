from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField 
from django.utils import timezone  
from home.models import EventYear

class Health_Safety_Guideline(models.Model):
    title =  models.CharField(max_length=250, null=False, blank=False, help_text='Code of Conduct PyCon Africa') 
    health_safety_guideline = MarkdownxField(default='', help_text = "[Supports Markdown] - COC PyCon Africa.", null=False, blank=False
                             )
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='health_safety_guideline',default=User) 
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="2024", related_name='health_safety_guidelines')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("health_safety_guideline")
 