# Core Django imports.
from django.contrib import admin

# Blog application imports.
from .models import FrequentlyAskedQuestion

class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):

    list_display = ('title', 'date_created')  
    ordering = ['-date_created', ]   

# Registers the FrequentlyAskedQuestionmodel at the admin backend.
admin.site.register(FrequentlyAskedQuestion, FrequentlyAskedQuestionAdmin)

