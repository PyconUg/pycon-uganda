from django.urls import path, include
from conference_schedule import views  # Update the import to reference the new app
from conference_schedule.views import ScheduleDetailView, create_talk_schedule  # Import views correctly
  

app_name = 'conference_schedule'  # Update the app name to reflect the new app

urlpatterns = [
    path('', views.schedule, name='schedule'),
    path('<slug:slug>/', ScheduleDetailView.as_view(), name='schedule_detail'), 
    # path('<slug:slug>/edit/', views.schedule_edit, name='schedule_edit'),  
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')), 
    path('create/', create_talk_schedule, name='create_talk_schedule'),
    path('new/', create_talk_schedule, name='create_new_talk_schedule'),
]
