from django import forms
from .models import Samochody, Wlasciciele, Czesci, Zlecenia, Operacje


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

class OperacjeForm(forms.ModelForm):
    rodzaj_operacji = forms.ChoiceField(choices=[('', 'Wybierz...'), ('c', 'Część'), ('u', 'Usługa'), ('i', 'Inne')])

    class Meta:
        model = Operacje
        fields = ['id_zlecenie', 'rodzaj_operacji', 'opis', 'id_czesc', 'cena_jednostkowa', 'ilosc', 'jednostka', 'stawka_vat']

    def __init__(self, *args, **kwargs):
        super(OperacjeForm, self).__init__(*args, **kwargs)
        self.fields['id_zlecenie'].widget = forms.HiddenInput()
        self.fields['id_czesc'] = forms.ModelChoiceField(
            queryset=Czesci.objects.all(),
            to_field_name="nazwa",
            required=False  # Opcjonalne, ustaw jeśli pole może być puste
        )

        # Jeśli rodzaj_operacji jest zdefiniowany, dostosuj dostępne opcje.
        if 'data' in kwargs:
            rodzaj_operacji = kwargs['data'].get('rodzaj_operacji')
            self._adjust_fields(rodzaj_operacji)
        elif self.instance.pk:
            self._adjust_fields(self.instance.rodzaj_operacji)

    def _adjust_fields(self, rodzaj_operacji):
        if rodzaj_operacji == 'c':
            self.fields['id_czesc'].queryset = Czesci.objects.all()
            self.fields['opis'].required = False
        elif rodzaj_operacji == 'u':
            self.fields['id_czesc'].required = False

