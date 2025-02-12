from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.page_view, name='page_view'),
]
