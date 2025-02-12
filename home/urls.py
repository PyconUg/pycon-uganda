from django.urls import path, include
from django.views.generic import TemplateView
from .views import *

from . import views


app_name = 'home' 
urlpatterns = [
    path('', homepage, name='homepage'),  
    path('<int:year>/', views.home_for_year, name='home_for_year'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),  
]

