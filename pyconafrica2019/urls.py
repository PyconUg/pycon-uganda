from django.urls import path
from . import views

from django.views.generic import TemplateView

app_name = 'pyconafrica2019'
urlpatterns = [
    path('', view=views.home19, name='home19'),
    path('about/', view=views.about, name='about'),
    path('report/', view=views.report, name='report'),
    path('schedule-19/', view=views.schedule, name='schedule'),
    path('conduct/', view=views.conduct, name='conduct'),
    path('coc/eporting-guidelines/', TemplateView.as_view(template_name='conduct/eporting-guidelines/eporting-guidelines.html')),
    path('coc/guidelines/', TemplateView.as_view(template_name='conduct/guidelines/guidelines.html')),
    path('sponsor-us-19/', view=views.sponsor_us, name='sponsor_us'),
    path('our-sponsors/', view=views.sponsors, name='sponsors'),
    path('register/', view=views.register, name='register'),
    path('travel/', view=views.traveladvice, name='traveladvice'),
    path('travel/guidance-international-visitors/', view=views.travelguide, name='travelguide'),
    path('fin-aid/', view=views.fin_aid, name='fin_aid'),
    path('team/', view=views.team, name='team'),
]

