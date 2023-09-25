from django import forms
from .models import Samochody, Wlasciciele, Czesci


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
