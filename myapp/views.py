import json

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Samochody, Czesci, Wlasciciele, Zlecenia, Operacje
from .forms import SamochodForm, WlascicielForm, CzesciForm, ZleceniaForm, OperacjeForm
from django.db.models import Q
from django.http import JsonResponse
from django.utils import timezone


def home(request):
    return render(request, 'home.html')

def my_view(request):
    # Pobranie zleceń, które mają czas rozpoczęcia, ale nie mają czasu zakończenia,
    # i których czas rozpoczęcia jest wcześniejszy niż obecna data.
    ongoing_orders = Zlecenia.objects.filter(
        czas_rozpoczecia__isnull=False,
        czas_zakonczenia__isnull=True,
        czas_rozpoczecia__lt=timezone.now()
    )

    # Przekazanie zleceń do kontekstu szablonu.
    context = {'ongoing_orders': ongoing_orders}

    return render(request, 'home.html', context)

def view_samochody(request):
    samochody = Samochody.objects.all()
    context = {
        'samochody': samochody
    }
    return render(request, 'samochody_list.html', context)

def add_samochod(request):
    if request.method == 'POST':
        form = SamochodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_samochody')
    else:
        form = SamochodForm()
    return render(request, 'add_edit_samochod.html', {'form': form})

def edit_samochod(request, samochod_id):
    samochod = get_object_or_404(Samochody, id=samochod_id)
    if request.method == 'POST':
        form = SamochodForm(request.POST, instance=samochod)
        if form.is_valid():
            form.save()
            return redirect('view_samochody')
    else:
        form = SamochodForm(instance=samochod)
    return render(request, 'add_edit_samochod.html', {'form': form})

def search_samochody(request):
    query = request.GET.get('q')
    samochody = Samochody.objects.order_by('-id')[:10]  # Get the last 10 created items
    if query:
        samochody = Samochody.objects.filter(
            Q(marka__icontains=query) |
            Q(model__icontains=query) |
            Q(nrrej__icontains=query) |
            Q(nrvin__icontains=query)
        )
    return render(request, 'samochody_list.html', {'samochody': samochody})

def search_samochody_wlasciciela(request, wlasciciel_id):
    samochody = Samochody.objects.filter(wlasciciel_id=wlasciciel_id)
    return render(request, 'samochody_list.html', {'samochody': samochody})

def delete_samochod(request, samochod_id):
    if request.method == 'POST':  # Upewnij się, że metoda żądania to POST
        samochod = get_object_or_404(Samochody, id=samochod_id)
        samochod.delete()
        return redirect('view_samochody')  # Zastąp to odpowiednim URL do strony listy samochodów
    else:
        return HttpResponse("Niepoprawne żądanie", status=405)

def view_wlasciciele(request):
    wlasciciele = Wlasciciele.objects.order_by('nazwisko')
    context = {
        'wlasciciele': wlasciciele
    }
    return render(request, 'wlasciciele.html', context)

def add_wlasciciel(request):
    if request.method == 'POST':
        form = WlascicielForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_wlasciciele')
    else:
        form = WlascicielForm()
    return render(request, 'add_edit_wlasciciel.html', {'form': form})

def edit_wlasciciel(request, wlasciciel_id):
    wlasciciel = get_object_or_404(Wlasciciele, id=wlasciciel_id)
    if request.method == 'POST':
        form = WlascicielForm(request.POST, instance=wlasciciel)
        if form.is_valid():
            form.save()
            return redirect('view_wlasciciele')
    else:
        form = WlascicielForm(instance=wlasciciel)
    return render(request, 'add_edit_wlasciciel.html', {'form': form})

def search_wlasciciele(request):
    query = request.GET.get('q')
    wlasciciele = Wlasciciele.objects.order_by('-id')[:10]  # Get the last 10 created items
    if query:
        wlasciciele = Wlasciciele.objects.filter(
            Q(imie__icontains=query) |
            Q(nazwisko__icontains=query) |
            Q(adres__icontains=query) |
            Q(email__icontains=query)
        )
    return render(request, 'wlasciciele.html', {'wlasciciele': wlasciciele})

def delete_wlasciciel(request, wlasciciel_id):
    if request.method == 'POST':  # Upewnij się, że metoda żądania to POST
        wlasciciel = get_object_or_404(Wlasciciele, id=wlasciciel_id)
        wlasciciel.delete()
        return redirect('view_wlasciciele')
    else:
        return HttpResponse("Niepoprawne żądanie", status=405)

def view_czesci(request):
    czesci = Czesci.objects.all()
    context = {
        'czesci': czesci
    }
    return render(request, 'czesci.html', context)

def add_czesc(request):
    if request.method == 'POST':
        form = CzesciForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_czesci')
    else:
        form = CzesciForm()
    return render(request, 'add_edit_czesc.html', {'form': form})

def edit_czesc(request, czesc_id):
    czesc = get_object_or_404(Czesci, id=czesc_id)
    if request.method == 'POST':
        form = CzesciForm(request.POST, instance=czesc)
        if form.is_valid():
            form.save()
            return redirect('view_czesci')
    else:
        form = CzesciForm(instance=czesc)
    return render(request, 'add_edit_czesc.html', {'form': form})

def zwieksz_ilosc_czesci(request):
    try:
        # Parse the JSON payload
        data = json.loads(request.body.decode('utf-8'))
        czesc_id = data.get('id')

        # Update the count in the database
        czesc = Czesci.objects.get(id=czesc_id)
        czesc.ilosc += 1
        czesc.save()

        return JsonResponse({'success': True})

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

def zmniejsz_ilosc_czesci(request):
    try:
        # Parse the JSON payload
        data = json.loads(request.body.decode('utf-8'))
        czesc_id = data.get('id')

        # Update the count in the database
        czesc = Czesci.objects.get(id=czesc_id)
        if czesc.ilosc > 0:
            czesc.ilosc -= 1
            czesc.save()

        return JsonResponse({'success': True})

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

def search_czesci(request):
    query = request.GET.get('q')
    czesci = Czesci.objects.order_by('-id')[:10]  # Get the last 10 created items
    if query:
        czesci = Czesci.objects.filter(
            Q(nazwa__icontains=query) |
            Q(cena_zakupu__icontains=query)
        )
    return render(request, 'czesci.html', {'czesci': czesci})

def delete_czesc(request, czesc_id):
    if request.method == 'POST':  # Upewnij się, że metoda żądania to POST
        czesc = get_object_or_404(Czesci, id=czesc_id)
        czesc.delete()
        return redirect('view_czesci')
    else:
        return HttpResponse("Niepoprawne żądanie", status=405)

def view_zlecenia(request):
    zlecenia = Zlecenia.objects.all()
    context = {
        'zlecenia': zlecenia
    }
    return render(request, 'zlecenia.html', context)

def add_zlecenie(request):
    if request.method == 'POST':
        form = ZleceniaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_zlecenia')
    else:
        form = ZleceniaForm()
    return render(request, 'add_edit_zlecenie.html', {'form': form})

def search_zlecenia(request):
    query = request.GET.get('q')
    zlecenia = Zlecenia.objects.order_by('-id')[:10]  # Get the last 10 created items
    if query:
        zlecenia = Zlecenia.objects.filter(
            Q(opis__icontains=query) |
            Q(czas_wprowadzenia__icontains=query) |
            Q(czas_rozpoczecia__icontains=query) |
            Q(czas_zakonczenia__icontains=query)
        )

    return render(request, 'zlecenia.html', {'zlecenia': zlecenia})

def search_zlecenia_dla_samochodu(request, samochod_id):
    samochod = get_object_or_404(Samochody, id=samochod_id)
    zlecenia = Zlecenia.objects.filter(nr_samochodu=samochod)
    return render(request, 'zlecenia.html', {'zlecenia': zlecenia})

def edit_zlecenie(request, zlecenie_id):
    zlecenie = get_object_or_404(Zlecenia, id=zlecenie_id)
    if request.method == 'POST':
        form = ZleceniaForm(request.POST, instance=zlecenie)
        if form.is_valid():
            form.save()
            return redirect('view_zlecenia')
    else:
        form = ZleceniaForm(instance=zlecenie)
    return render(request, 'add_edit_zlecenie.html', {'form': form})

def search_operacje_dla_zlecenia(request, zlecenie_id):
    operacje = Operacje.objects.filter(id_zlecenie=zlecenie_id)
    suma = sum(op.ilosc * op.cena_jednostkowa for op in operacje)
    context = {
        'operacje': operacje,
        'zlecenie_id': zlecenie_id,
        'suma': suma,
    }
    return render(request, 'operacje.html', context)

def add_operacja_dla_zlecenia(request, zlecenie_id):
    if request.method == 'POST':
        form = OperacjeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search_operacje_dla_zlecenia', zlecenie_id=zlecenie_id)
        else:
            print("Form errors: ", form.errors)
            print("POST data: ", request.POST)
    else:
        form = OperacjeForm(initial={'id_zlecenie': zlecenie_id})
    return render(request, 'add_edit_operacje.html', {'form': form, 'zlecenie_id': zlecenie_id})
