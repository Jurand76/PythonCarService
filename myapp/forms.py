from django import forms
from .models import Samochody, Wlasciciele, Czesci, Zlecenia


class SamochodForm(forms.ModelForm):
    class Meta:
        model = Samochody
        fields = ['marka', 'model', 'nrvin', 'nrrej', 'wlasciciel']
        labels = {
            'nrvin': 'Numer nadwozia',
            'wlasciciel': 'Właściciel',
            'nrrej': 'Numer rejestracyjny'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['wlasciciel'].queryset = Wlasciciele.objects.order_by('nazwisko')


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
