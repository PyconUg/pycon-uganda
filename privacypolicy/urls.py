from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'privacypolicy'
urlpatterns = [
    path('', view=views.privacypolicy, name='privacypolicy'),
]
