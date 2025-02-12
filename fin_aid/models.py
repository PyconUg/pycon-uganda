from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField 
from django.utils import timezone  
from home.models import EventYear

class Fin_aid(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False, help_text='Financial Assistance PyCon Africa') 
    financial_assistance = MarkdownxField(default='', help_text="[Supports Markdown] - Financial Assistance PyCon Africa.", null=False, blank=False)
    google_form_formfacade_code = models.TextField(default='', help_text='Link to your google form', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fin_aid', default=User)
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="2024", related_name='fin_aids')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    fin_open_date = models.DateTimeField(help_text='Date and time when the financial aid form opens', null=False, blank=False, default=timezone.now)
    fin_close_date = models.DateTimeField(help_text='Date and time when the financial aid form closes', null=False, blank=False, default=timezone.now)

    class Meta:
        permissions = [
            ("can_edit_fin_aid", "Can edit financial aid form"),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("fin_aid_detail", kwargs={"pk": self.pk})

    def is_form_open(self):
        now = timezone.now()
        return self.fin_open_date <= now <= self.fin_close_date

    def is_form_closed(self):
        now = timezone.now()
        return now > self.fin_close_date

    def is_form_not_open_yet(self):
        now = timezone.now()
        return now < self.fin_open_date

    def get_form_status_message(self):
        if self.is_form_not_open_yet():
            return "The financial aid application form will open on {}".format(self.fin_open_date.strftime("%Y-%m-%d %H:%M:%S"))
        elif self.is_form_closed():
            return "The financial aid application form closed on {}".format(self.fin_close_date.strftime("%Y-%m-%d %H:%M:%S"))
        else:
            return "The financial aid application form is currently open."