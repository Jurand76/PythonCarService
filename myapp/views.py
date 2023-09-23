from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Samochody
from .forms import SamochodForm
from django.db.models import Q
from .models import Wlasciciele


def home(request):
    return render(request, 'home.html')

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
            return redirect('view_samochody_list')
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