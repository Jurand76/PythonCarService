from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('samochody/', views.view_samochody, name='view_samochody'),
]
