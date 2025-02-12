from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'page_title', 'slug', 'created_at', 'updated_at')
    search_fields = ('page_name', 'content')
