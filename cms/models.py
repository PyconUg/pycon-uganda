from django.db import models
from django.conf import settings
from markdownx.models import MarkdownxField 
from home.models import EventYear
import os
from django.utils.text import slugify


class Page(models.Model):
    page_name = models.CharField(max_length=200, default='')
    page_title =  models.CharField(max_length=200, default='')
    meta_og_image = models.ImageField(help_text="Upload your cover image or leave blank to use our default image", default="meta-image.png", null=True, blank=True, upload_to='ticket_page')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    font_icon_code = models.CharField(max_length=200, default='fa-brands fa-python', help_text = "The font icon for the page, use the following format - fa-brands fa-python")
    content = MarkdownxField(default='', help_text = "[Supports Markdown] - Content for the page", null=False, blank=False)
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="2025", related_name='pages')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = slugify(self.page_name)
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return self.page_name
    
    @property
    def image_url(self):
        if self.meta_og_image:
            return self.meta_og_image.url
        return os.path.join(settings.STATIC_URL, 'default_image.png')
