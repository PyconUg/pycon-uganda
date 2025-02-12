from django.shortcuts import render, get_object_or_404
from .models import Page
from home.models import EventYear
from django.utils.html import strip_tags

def page_view(request, year, slug):
    event_year = get_object_or_404(EventYear, year=year)
    page = get_object_or_404(Page, slug=slug, event_year=event_year)

    # Generate metadata if not explicitly provided
    meta_title = page.meta_title or page.page_title or page.page_name
    meta_description = page.meta_description or strip_tags(page.content)[:160]  # Get the first 160 characters of content as a description
    meta_author = page.meta_author or "PyCon Africa"
    meta_og_image = page.meta_og_image or 'default_image_url'  # Provide a default image URL if not set

    context = {
        'page': page,
        'meta_title': meta_title,
        'meta_description': meta_description,
        'meta_author': meta_author,
        'meta_og_image': meta_og_image,
    }
    template_name = f'{year}/pages/page.html'
    return render(request, template_name, context)

def page_view(request, year, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, f'{year}/pages/page.html', {'page': page})
