from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django_extensions.db.fields import AutoSlugField
from django_slugify_processor.text import slugify
from django.contrib.contenttypes.fields import GenericRelation 
 
from six import python_2_unicode_compatible
from tinymce.models import HTMLField

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
@python_2_unicode_compatible
 

class PyConEvent(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    flag_image = models.ImageField(upload_to='countryflags/',default="flag.jpg")
    city = models.CharField(max_length=255, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    year = models.IntegerField()  # Year of the Conference
    website_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} {self.year}"

    class Meta:
        ordering = ['start_date']


class EventYear(models.Model):
    year = models.IntegerField(unique=True)
    home_info = models.TextField(blank=True, null=True)
    template_path = models.CharField(max_length=255, default="home/home.html", help_text="Path to the year's templates, e.g., '2020/home/home.html'")

    def __str__(self):
        return f"PyCon Africa {self.year}"

    class Meta:
        verbose_name = 'Event Year'
        verbose_name_plural = 'Event Years'