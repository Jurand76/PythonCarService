from django.utils import timezone
from .models import Zlecenia, Samochody

def ongoing_orders(request):
    orders = Zlecenia.objects.filter(
        czas_rozpoczecia__isnull=False,
        czas_zakonczenia__isnull=True,
        czas_rozpoczecia__lt=timezone.now()
    )

    order_details = []
    for order in orders:
        order_details.append({
            'order': order,
            'marka': order.nr_samochodu.marka,
            'model': order.nr_samochodu.model,
            'nrrej': order.nr_samochodu.nrrej,
        })

    return {'order_details': order_details}
