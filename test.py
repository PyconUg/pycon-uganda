#!/usr/bin/env python
"""
Run a quick email test using the project's Django settings and backend.

Usage:
  python test.py
  python test.py someone@example.com

Requires Django (run from project root, with venv activated).
"""
import os
import sys

# Use project settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyconafrica.settings")

def main():
    import django
    django.setup()
    from django.conf import settings
    from django.core.mail import send_mail

    recipient = sys.argv[1] if len(sys.argv) > 1 else settings.DEFAULT_FROM_EMAIL

    print("Email test")
    print("  Backend:", settings.EMAIL_BACKEND)
    print("  From:", settings.DEFAULT_FROM_EMAIL)
    print("  To:", recipient)
    if hasattr(settings, "EMAIL_HOST"):
        print("  Host:", getattr(settings, "EMAIL_HOST", "—"))
        print("  Port:", getattr(settings, "EMAIL_PORT", "—"))
        print("  SSL:", getattr(settings, "EMAIL_USE_SSL", "—"))
        print("  TLS:", getattr(settings, "EMAIL_USE_TLS", "—"))
    print()

    try:
        send_mail(
            subject="[PyCon Africa 2026] Email test",
            message="If you received this, the email backend is working.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient],
            fail_silently=False,
        )
        print("OK: Message sent to", recipient)
    except Exception as e:
        print("FAIL:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
