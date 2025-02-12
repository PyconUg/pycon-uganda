from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'faq'
urlpatterns = [
    path('', view=views.faq, name='faq'),
]
