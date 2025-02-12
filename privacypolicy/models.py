from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField 
from django.utils import timezone  
from home.models import EventYear

class PrivacyPolicy(models.Model):
    title =  models.CharField(max_length=250, null=False, blank=False, help_text='Privacy policies of PyCon Africa') 
    privacy_policy = MarkdownxField(default='', help_text = "[Supports Markdown] - COC PyCon Africa.", null=False, blank=False
                             )
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='privacypolicy',default=User) 
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="2024", related_name='privacypolicies')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    
    class Meta:
        unique_together = ('title',)
        verbose_name = 'privacypolicy'
        verbose_name_plural = 'privacypolicies'


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("privacypolicies")
 