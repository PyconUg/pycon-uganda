from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from .views import *
from . import views
from speakers.views import SpeakerDetailView

app_name = 'registration'

urlpatterns = [  
    path('create_profile/', login_required(CreateProfileView.as_view()), name='create_profile'),
    path('update/<str:pk>/', UpdateProfileView.as_view(), name='profile_update'),  
    path('', login_required(ProfileView.as_view()), name='profile_home'),
    re_path('password_change/(?P<pk>\d+)/', login_required(PasswordView.as_view()), name='password_change'),
    re_path('login_details/(?P<pk>\d+)/', login_required(UpdateLoginView.as_view()), name='login_details'),
    path('profile_updated/', login_required(SuccessView.as_view()), name='profile_update'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
