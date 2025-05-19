from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('pyladies/', views.pyladies, name='pyladies'),
    path('django-girls/', views.django_girls, name='django_girls'),
]