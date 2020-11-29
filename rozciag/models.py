from django.db import models
from datetime import datetime
import socket
import getpass
from django.contrib.auth.models import User


class GrupaRobocza(models.Model):
    nazwa = models.CharField(max_length=15)
    aktywna = models.BooleanField(default=True)

    def __str__(self):
        return self.nazwa


class Narzedzia(models.Model):
    grupa = models.CharField(max_length=15)
    uwagi = models.CharField(max_length=150,null=True,blank=True)
    aktywny = models.BooleanField(default=True)

    def __str__(self):
        return self.grupa


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dzial = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Rozciagi(models.Model):

    hostname = socket.gethostname()
    login_username = getpass.getuser()
    user = User.username

    listy = (
        ('lista',"Lista połączeń"),
        ('zlecenie', "Zlecenie produkcyjne")
    )

    nr_zlecenia = models.CharField(max_length=10)#
    #nr_pozycji = models.DecimalField(max_digits=4,decimal_places=0)#
    nr_pozycji = models.CharField(max_length=200)#
    lista = models.CharField(max_length=15, default="lista", choices=listy)#
    nr_pracownika = models.DecimalField(max_digits=5,decimal_places=0)#
    rozciag = models.DecimalField(max_digits=5,decimal_places=0)#
    przekroj_przewodu = models.DecimalField(max_digits=4,decimal_places=2)#
    indeks_kontaktu = models.CharField(max_length=10)#
    poprawkowe = models.BooleanField(default=False)#
    narzedzia = models.CharField(max_length=20)#
    grupa_robocza = models.ForeignKey(GrupaRobocza, on_delete=models.CASCADE)#
    wysokosc = models.DecimalField(max_digits=4,decimal_places=2,default=0, blank=True, null=True)#
    data_serwis = models.DateTimeField('data serwis', blank=True, null=True)
    data_dodania = models.DateTimeField('data dodania',default=datetime.now)
    narzedzia_rodzaj = models.ForeignKey(Narzedzia, on_delete=models.CASCADE)#
    potwierdzenie = models.BooleanField(default=False)
    zalogowany_user = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    komputer_user = models.CharField(max_length=10,default=login_username)
    komputer = models.CharField(max_length=30,default=hostname)


    def __str__(self):
        return self.indeks_kontaktu

