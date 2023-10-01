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
        fields = ['nazwa', 'cena_zakupu', 'ilosc', 'jednostka', 'stawka_vat']

class ZleceniaForm(forms.ModelForm):
    class Meta:
        model = Zlecenia
        fields = ['nr_samochodu', 'czas_wprowadzenia', 'czas_rozpoczecia', 'czas_zakonczenia', 'opis', 'przebieg']
