from django.contrib import admin
from django.contrib.sites.shortcuts import get_current_site

from markdownx.admin import MarkdownxModelAdmin
from .models import RegistrationProfile, Profile
from .users import UsernameField
from .utils import _
from django.utils.html import format_html


class SpeakerInline(admin.StackedInline):
    model = Profile
    extra = 0
    

class RegistrationAdmin(admin.ModelAdmin):
    actions = ['activate_users', 'resend_activation_email']
    list_display = ('user', 'activation_key_expired')
    raw_id_fields = ['user']
    search_fields = ('user__{0}'.format(UsernameField()),
                     'user__first_name', 'user__last_name')

    def activate_users(self, request, queryset):
        """
        Activates the selected users, if they are not already
        activated.

        """

        site = get_current_site(request)
        for profile in queryset:
            RegistrationProfile.objects.activate_user(profile.activation_key, site)
    activate_users.short_description = _("Activate users")

    def resend_activation_email(self, request, queryset):
        """
        Re-sends activation emails for the selected users.

        Note that this will *only* send activation emails for users
        who are eligible to activate; emails will not be sent to users
        whose activation keys have expired or who have already
        activated.

        """

        site = get_current_site(request)
        for profile in queryset:
            user = profile.user
            RegistrationProfile.objects.resend_activation_mail(user.email, site, request)

    resend_activation_email.short_description = _("Re-send activation emails")


admin.site.register(RegistrationProfile, RegistrationAdmin)


class PersonalAdmin(admin.ModelAdmin):
    list_display = (
        "profile_picture_thumbnail",  "name", "surname", "user", "is_visible", 
        'is_a_sponsor_or_keynote_speaker', 'profession', 'organization',  
        'contact_number', 'city', 'country', 'date_created', 'updated'
    )
    list_editable = ["is_visible", 'is_a_sponsor_or_keynote_speaker'] 
    ordering = ['-date_created']

    def profile_picture_thumbnail(self, obj):
        if obj.profile_image:
            return format_html(
                '<img src="{}" width="40" height="40" style="border-radius:50%;" />',
                obj.profile_image.url
            )
        return "No Image"

    profile_picture_thumbnail.short_description = 'Profile Picture'

admin.site.register(Profile, PersonalAdmin)
 