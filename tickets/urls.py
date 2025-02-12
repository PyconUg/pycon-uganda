from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'tickets'
urlpatterns = [
    path('', view=views.ticket, name='ticket'),
    path('register', view=views.register, name='register'),
]
