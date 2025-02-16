import os
import django

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyconafrica.settings")
django.setup()

from django.db import IntegrityError
from django.core.management import call_command
from home.models import EventYear
from cms.models import Page



# Handle migrations
try:
    call_command("makemigrations","home", "cms", "coc", "fin_aid", "registration", "talks", "about", "conference_schedule", "health_safety_guideline","privacypolicy","speakers","sponsor_us","tickets")
    call_command("migrate")
    print("Migrations completed successfully.")
except Exception as e:
    print(f"An error occurred while running migrations: {e}")

# Create EventYear and Pages
try:
    event_year, created = EventYear.objects.get_or_create(
        year=2025,
        defaults={"home_info": "This is the 2025 event year", "template_path": "home/2025/home.html"}
    )
    
    if created:
        print("Event Year created successfully")
    else:
        print(f"Event Year {event_year.year} already exists.")

    page, page_created = Page.objects.get_or_create(
        page_name="home",
        defaults={"page_title": "Home", "content": "This is the home page", "event_year": event_year}
    )

    if page_created:
        print("Page created successfully")
    else:
        print(f"Page '{page.page_name}' already exists for event year {event_year.year}.")

except IntegrityError as e:
    print(f"Database error: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
