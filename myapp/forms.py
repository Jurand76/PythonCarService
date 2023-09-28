from django import forms
from .models import Samochody, Wlasciciele, Czesci, Zlecenia


class SamochodForm(forms.ModelForm):
    class Meta:
        model = Samochody
        fields = ['marka', 'model', 'nrvin', 'nrrej', 'wlasciciel']


class WlascicielForm(forms.ModelForm):
    class Meta:
        model = Wlasciciele
        fields = ['imie', 'nazwisko', 'adres', 'telefon', 'email']

class CzesciForm(forms.ModelForm):
    class Meta:
        model = Czesci
        fields = ['nazwa', 'cena_zakupu', 'ilosc', 'jednostka', 'stawka']

class ZleceniaForm(forms.ModelForm):
    class Meta:
        model = Zlecenia
        fields = ['nr_samochodu', 'data_wprowadzenia', 'data_rozpoczecia', 'data_zakonczenia', 'opis', 'przebieg']
