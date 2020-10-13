from django.contrib import admin
from .models import Rozciagi, Narzedzia, Author, GrupaRobocza

@admin.register(GrupaRobocza)
class GrupaRoboczaAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'aktywna')
    list_filter = ('nazwa', 'aktywna')
    search_fields = ('nazwa', 'aktywna')

@admin.register(Narzedzia)
class NarzedziaAdmin(admin.ModelAdmin):
    list_display = ('grupa', 'uwagi', 'aktywny')
    list_filter = ('grupa', 'uwagi', 'aktywny')
    search_fields = ('grupa', 'uwagi', 'aktywny')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'dzial')
    list_filter = ('user', 'dzial')
    search_fields = ('user', 'dzial')


@admin.register(Rozciagi)
class RozciagiAdmin(admin.ModelAdmin):
    list_display = (
        'nr_zlecenia',
        'nr_pozycji',
        'nr_pracownika',
        'rozciag',
        'przekroj_przewodu',
        'indeks_kontaktu',
        'poprawkowe',
        'narzedzia',
        'grupa_robocza',
        'data_dodania',
        'narzedzia_rodzaj',
        'potwierdzenie',
        'zalogowany_user',
        'komputer_user',
        'komputer'
    )
    list_filter = (
        'nr_zlecenia',
        'nr_pozycji',
        'nr_pracownika',
        'rozciag',
        'przekroj_przewodu',
        'indeks_kontaktu',
        'poprawkowe',
        'narzedzia',
        'data_dodania',
        'narzedzia_rodzaj',
        'potwierdzenie',
        'zalogowany_user',
        'komputer_user',
        'komputer'
    )
    search_fields = (
        'nr_zlecenia',
        'nr_pozycji',
        'nr_pracownika',
        'rozciag',
        'przekroj_przewodu',
        'indeks_kontaktu',
        'poprawkowe',
        'narzedzia',
        'data_dodania',
        'narzedzia_rodzaj',
        'potwierdzenie',
        'zalogowany_user',
        'komputer_user',
        'komputer'
    )


