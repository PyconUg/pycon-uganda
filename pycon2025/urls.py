from django.urls import path
from . import views

from django.views.generic import TemplateView

app_name = 'pycon2025'
urlpatterns = [
    path('', view=views.home2025, name='home2025'),
    path('about/', view=views.about, name='about'), 
    path('conduct/', view=views.conduct, name='conduct'),
    path('coc/eporting-guidelines/', TemplateView.as_view(template_name='conduct/eporting-guidelines/eporting-guidelines.html')),
    path('coc/guidelines/', TemplateView.as_view(template_name='conduct/guidelines/guidelines.html')),
    path('sponsor-us/', view=views.sponsor_us, name='sponsor_us'),
    path('speakers_list/', view=views.speakers, name='speakers'),
    path('schedule/', view=views.scheduIe, name='schedule'),
    path('our-sponsors/', view=views.sponsors, name='sponsors'),
    path('register/', view=views.register, name='register'),
    path('travel/', view=views.traveladvice, name='traveladvice'),
    # path('fin-aid/', view=views.fin_aid, name='fin_aid'),
    path('team/', view=views.team, name='team'),
    path('report/', view=views.report, name='report'),
    path('platform/', view=views.hopin, name='hopin'), 
    # path('community/pyladies/', view=views.pyladies, name='pyladies'),
    path('community/django-girls/', view=views.django_girls, name='django_girls'),
    path('community/pyladies-wksp/', view=views.pyladies_wksp, name='pyladies_wksp'),   
    path('community/ngombor/', view=views.ngombor, name='ngombor')
]

