from django.urls import path
from . import views

app_name = 'sponsors'
urlpatterns = [
    path('', views.sponsors, name='sponsors'),
    path('<slug:slug>/', views.sponsor_detail, name='sponsor_detail'),
    path('prospectus', views.Prospectus, name='Prospectus')
]
