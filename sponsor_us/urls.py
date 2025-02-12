from django.urls import path
from . import views 

app_name = 'sponsor_us'


urlpatterns = [
    path('', views.sponsor_us, name='sponsor_us'),
    path('thank-you', views.thank_you, name='thank_you')
]