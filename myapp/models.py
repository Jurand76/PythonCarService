# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Wlasciciele(models.Model):
    imie = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')
    nazwisko = models.CharField(max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    adres = models.CharField(max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    telefon = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    email = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    def __str__(self):
        return f'{self.nazwisko} {self.imie}'

    class Meta:
        managed = False
        db_table = 'wlasciciele'

class Samochody(models.Model):
    wlasciciel = models.ForeignKey('Wlasciciele', models.DO_NOTHING, db_column='wlasciciel', blank=True, null=True)
    marka = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    nrvin = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    nrrej = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'samochody'
class Zlecenia(models.Model):
    nr_samochodu = models.ForeignKey(Samochody, models.DO_NOTHING, db_column='nr_samochodu')
    opis = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    czas_wprowadzenia = models.DateField()
    czas_rozpoczecia = models.DateField(blank=True, null=True)
    czas_zakonczenia = models.DateField(blank=True, null=True)
    przebieg = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zlecenia'

class Czesci(models.Model):
    nazwa = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    cena_zakupu = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ilosc = models.IntegerField()
    jednostka = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    stawka_vat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'czesci'


class Operacje(models.Model):
    id_zlecenie = models.ForeignKey('Zlecenia', models.DO_NOTHING, db_column='id_zlecenie')
    id_czesc = models.ForeignKey(Czesci, models.DO_NOTHING, db_column='id_czesc', blank=True, null=True)
    rodzaj_operacji = models.CharField(max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS')
    ilosc = models.IntegerField()
    jednostka = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    cena_jednostkowa = models.DecimalField(max_digits=10, decimal_places=2)
    stawka_vat = models.IntegerField()
    opis = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operacje'




