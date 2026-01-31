from django.urls import path
from . import views

from django.views.generic import TemplateView

app_name = 'pycon2026'
urlpatterns = [
    path('', view=views.home2026, name='home2026'),
    path('about/', view=views.about, name='about'),
    path('about/pycon-africa-2026/', view=views.about_pycon_africa_2026, name='about_pycon_africa_2026'),
    path('about/kenya-region/', view=views.about_kenya_region, name='about_kenya_region'),
    path('about/rwanda-region/', view=views.about_rwanda_region, name='about_rwanda_region'),
    path('about/tanzania-region/', view=views.about_tanzania_region, name='about_tanzania_region'),
    path('about/south-sudan-region/', view=views.about_south_sudan_region, name='about_south_sudan_region'), 
    path('conduct/', view=views.conduct, name='conduct'),
    path('coc/', view=views.coc, name='coc'),
    path('coc/eporting-guidelines/', TemplateView.as_view(template_name='conduct/eporting-guidelines/eporting-guidelines.html')),
    path('coc/guidelines/', TemplateView.as_view(template_name='conduct/guidelines/guidelines.html')),
    path('sponsor-us/', view=views.sponsor_us, name='sponsor_us'),
    path('speakers_list/', view=views.speakers, name='speakers'),
    path('schedule/', view=views.scheduIe, name='schedule'),
    path('our-sponsors/', view=views.sponsors, name='sponsors'),
    path('register/', view=views.register, name='register'),
    path('travel/', view=views.traveladvice, name='traveladvice'),
    path('visa/apply/', view=views.visa_apply, name='applying_for_visa'),
    path('visa/letter/', view=views.visa_letter, name='visa_letter'),
    # path('fin-aid/', view=views.fin_aid, name='fin_aid'),
    path('team/', view=views.team, name='team'),
    path('report/', view=views.report, name='report'),
    path('platform/', view=views.hopin, name='hopin'), 
    # path('community/pyladies/', view=views.pyladies, name='pyladies'),
    path('community/django-girls/', view=views.django_girls, name='django_girls'),
    path('community/pyladies-wksp/', view=views.pyladies_wksp, name='pyladies_wksp'),   
    # path('community/ngombor/', view=views.ngombor, name='ngombor')
]


