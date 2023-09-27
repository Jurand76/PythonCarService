from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('samochody/', views.view_samochody, name='view_samochody'),
    path('samochody/add/', views.add_samochod, name='add_samochod'),
    path('samochody/edit/<int:samochod_id>/', views.edit_samochod, name='edit_samochod'),
    path('samochody/search/', views.search_samochody, name='search_samochody'),
    path('samochody/wlasciciel/<int:wlasciciel_id>/', views.search_samochody_wlasciciela, name='search_samochody_wlasciciela'),
    path('wlasciciele/', views.view_wlasciciele, name='view_wlasciciele'),
    path('wlasciciele/add/', views.add_wlasciciel, name='add_wlasciciel'),
    path('wlasciciele/edit/<int:wlasciciel_id>/', views.edit_wlasciciel, name='edit_wlasciciel'),
    path('wlasciciele/search/', views.search_wlasciciele, name='search_wlasciciele'),
    path('czesci/', views.view_czesci, name='view_czesci'),
    path('czesci/add/', views.add_czesc, name='add_czesc'),
    path('czesci/search/', views.search_czesci, name='search_czesci'),
    path('zlecenia/', views.view_zlecenia, name='view_zlecenia'),
    path('zlecenia/add/', views.add_zlecenie, name='add_zlecenie'),
    path('zlecenia/search/', views.search_zlecenia, name='search_zlecenia'),
]
