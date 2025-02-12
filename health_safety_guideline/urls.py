from django.urls import path
from . import views

app_name = 'health_safety_guideline'
urlpatterns = [
    path('', views.health_safety_guideline, name='health_safety_guideline')
]