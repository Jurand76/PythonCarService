from django.contrib import admin

# Register your models here.

from .models import Samochody, Wlasciciele, Czesci, Zlecenia, Operacje

admin.site.register(Samochody)
admin.site.register(Wlasciciele)
admin.site.register(Czesci)
admin.site.register(Zlecenia)
admin.site.register(Operacje)
