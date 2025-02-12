from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField 
from django.utils import timezone  
from home.models import EventYear


class FrequentlyAskedQuestion(models.Model):
    title =  models.CharField(max_length=250, null=False, blank=False, help_text='FAQs PyCon Africa') 
    faqs = MarkdownxField(default='', help_text = "[Supports Markdown] - FAQs PyCon Africa.", null=False, blank=False
                             )
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='faq',default=User) 
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="2024", related_name='faqs')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("faqs")
 