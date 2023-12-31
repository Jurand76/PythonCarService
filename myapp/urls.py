from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('samochody/', views.view_samochody, name='view_samochody'),
    path('samochody/add/', views.add_samochod, name='add_samochod'),
    path('samochody/edit/<int:samochod_id>/', views.edit_samochod, name='edit_samochod'),
    path('samochody/search/', views.search_samochody, name='search_samochody'),
    path('samochody/wlasciciel/<int:wlasciciel_id>/', views.search_samochody_wlasciciela, name='search_samochody_wlasciciela'),
    path('samochody/delete/<int:samochod_id>/', views.delete_samochod, name='delete_samochod'),
    path('wlasciciele/', views.view_wlasciciele, name='view_wlasciciele'),
    path('wlasciciele/add/', views.add_wlasciciel, name='add_wlasciciel'),
    path('wlasciciele/edit/<int:wlasciciel_id>/', views.edit_wlasciciel, name='edit_wlasciciel'),
    path('wlasciciele/search/', views.search_wlasciciele, name='search_wlasciciele'),
    path('wlasciciele/delete/<int:wlasciciel_id>/', views.delete_wlasciciel, name='delete_wlasciciel'),
    path('czesci/', views.view_czesci, name='view_czesci'),
    path('czesci/add/', views.add_czesc, name='add_czesc'),
    path('czesci/edit/<int:czesc_id>/', views.edit_czesc, name='edit_czesc'),
    path('czesci/search/', views.search_czesci, name='search_czesci'),
    path('czesci/zwieksz/', views.zwieksz_ilosc_czesci, name='zwieksz_ilosc_czesci'),
    path('czesci/zmniejsz/', views.zmniejsz_ilosc_czesci, name='zmniejsz_ilosc_czesci'),
    path('czesci/delete/<int:czesc_id>/', views.delete_czesc, name='delete_czesc'),
    path('zlecenia/', views.view_zlecenia, name='view_zlecenia'),
    path('zlecenia/add/', views.add_zlecenie, name='add_zlecenie'),
    path('zlecenia/edit/<int:zlecenie_id>', views.edit_zlecenie, name='edit_zlecenie'),
    path('zlecenia/search/', views.search_zlecenia, name='search_zlecenia'),
    path('zlecenia/<int:samochod_id>/', views.search_zlecenia_dla_samochodu, name='search_zlecenia_dla_samochodu'),
    path('zlecenia/details/<int:zlecenie_id>', views.search_operacje_dla_zlecenia, name='search_operacje_dla_zlecenia'),
    path('operacja/add/<int:zlecenie_id>', views.add_operacja_dla_zlecenia, name='add_operacja_dla_zlecenia'),
    path('wydruk/<int:zlecenie_id>/', views.zlecenie_wydruk, name='zlecenie_wydruk'),
]
 