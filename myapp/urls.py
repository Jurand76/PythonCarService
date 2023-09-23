from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('samochody/', views.view_samochody, name='view_samochody'),
    path('samochody/add/', views.add_samochod, name='add_samochod'),
    path('samochody/edit/<int:samochod_id>/', views.edit_samochod, name='edit_samochod'),
    path('samochody/search/', views.search_samochody, name='search_samochody'),
]
