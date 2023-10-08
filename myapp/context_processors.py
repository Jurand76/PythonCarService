from django.utils import timezone
from .models import Zlecenia, Samochody

def ongoing_orders(request):
    orders = Zlecenia.objects.filter(
        czas_rozpoczecia__isnull=False,
        czas_zakonczenia__isnull=True,
        czas_rozpoczecia__lt=timezone.now()
    )

    ongoing_orders = []
    for order in orders:
        ongoing_orders.append({
            'order': order,
            'marka': order.nr_samochodu.marka,
            'model': order.nr_samochodu.model,
            'nrrej': order.nr_samochodu.nrrej,
        })

    return {'ongoing_orders': ongoing_orders}

def finished_orders(request):
    orders = Zlecenia.objects.filter(
        czas_rozpoczecia__isnull=False,
        czas_zakonczenia__isnull=False,
    )

    finished_orders = []
    for order in orders:
        finished_orders.append({
            'order': order,
            'marka': order.nr_samochodu.marka,
            'model': order.nr_samochodu.model,
            'nrrej': order.nr_samochodu.nrrej,
        })

    return {'finished_orders': finished_orders}

def future_orders(request):
    orders = Zlecenia.objects.filter(
        czas_rozpoczecia__isnull=True,
        czas_zakonczenia__isnull=True,
    )

    future_orders = []
    for order in orders:
        future_orders.append({
            'order': order,
            'marka': order.nr_samochodu.marka,
            'model': order.nr_samochodu.model,
            'nrrej': order.nr_samochodu.nrrej,
        })

    return {'future_orders': future_orders}
