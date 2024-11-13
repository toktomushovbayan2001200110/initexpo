# urls.py
from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.index, name='home'),  # Ensure this line exists
    path('about/', views.about, name='about'),

    # Other URL patterns
]
