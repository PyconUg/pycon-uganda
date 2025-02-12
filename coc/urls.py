from django.urls import path
from . import views

app_name = 'coc'
urlpatterns = [
    path('', views.coc, name='coc')
    
]