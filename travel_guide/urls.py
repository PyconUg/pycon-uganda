from django.urls import path
from . import views

app_name = 'travel_guide'

urlpatterns = [
    path('', views.travel_guide, name='travel_guide'),
]