from django.conf.urls.static import static
from django.contrib import admin 
from django.urls import include, path, re_path
from . import views
from .views import AboutView 
from .views import *
from django.conf import settings
from django.contrib.auth.decorators import login_required

app_name = 'about'
urlpatterns = [ 
    # Adjusted to include a year parameter
    path('', view=views.about, name='about_home'),     
    path('<int:year>/about/update/<int:pk>/edit/', views.about_edit, name='about_edit'),
    
    
    # Adjusted team, venue, and travel advice URLs to include a year parameter
    path('team/', teams_view, name='team'),
    path('venue/', view=views.venue, name='venue'),
    path('travel-advice/', view=views.travel_advice, name='travel_advice'),
    path('platform/', view=views.hopin, name='hopin'), 
]
