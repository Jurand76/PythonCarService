from django import forms
from .models import Samochody, Wlasciciele


class SamochodForm(forms.ModelForm):
    class Meta:
        model = Samochody
        fields = ['marka', 'model', 'nrvin', 'nrrej', 'wlasciciel']


class WlascicielForm(forms.ModelForm):
    class Meta:
        model = Wlasciciele
        fields = ['imie', 'nazwisko', 'adres', 'telefon', 'email']
