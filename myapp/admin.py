from django.contrib import admin

# Register your models here.

from .models import Samochody, Wlasciciele, Czesci, Zlecenia

admin.site.register(Samochody)
admin.site.register(Wlasciciele)
admin.site.register(Czesci)
admin.site.register(Zlecenia)
