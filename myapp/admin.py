from django.contrib import admin

# Register your models here.

from .models import Samochody, Wlasciciele, Czesci

admin.site.register(Samochody)
admin.site.register(Wlasciciele)
admin.site.register(Czesci)
