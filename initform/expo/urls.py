from django.urls import path
from . import views

urlpatterns = [
    path('', views.expo, name='expo'),
    path('register/', views.register_participant, name='register_participant'),
    path('participants/', views.participants_by_section, name='participants_by_section'),
]
