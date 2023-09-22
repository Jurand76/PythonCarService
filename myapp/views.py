from django.shortcuts import render
from django.http import HttpResponse
from .models import Samochody
from .models import Wlasciciele


def home(request):
    return render(request, 'home.html')

def view_samochody(request):
    samochody = Samochody.objects.all()
    context = {
        'samochody': samochody
    }
    return render(request, 'samochody_list.html', context)

