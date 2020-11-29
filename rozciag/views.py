from django.shortcuts import render, redirect, get_object_or_404
from .models import Rozciagi, Author, User
from .forms import RozciagiForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponse
import csv
from datetime import datetime

def get_author(user):
    if user.is_anonymous:
        guest_user = User.objects.get(username="guest")  # or whatever ID or name you use for the placeholder user that no one will be assigned
        qs = Author.objects.filter(user=guest_user)
        if qs.exists():
            return qs[0]
        return None
    else:
        qs = Author.objects.filter(user=user)
        if qs.exists():
            return qs[0]
        return None


def wszystkie_wpisy(request):
    rozciag = Rozciagi.objects.all().order_by('-id')[:1000]

    context = {
        'rozciag': rozciag
    }

    return render(request, 'rozciagi/wszystkie_wpisy.html', context)


def nowy_wpis(request):
    form = RozciagiForm(request.POST or None, request.FILES or None)
    data_dodania = datetime.now()

    if form.is_valid():
        author = get_author(request.user)
        print(author)
        form.instance.zalogowany_user = author
        form.save()
        messages.info(request, f"Dane zostały zapisane.")
        return redirect(nowy_wpis)

    context = {
        'form': form
    }

    return render(request, 'rozciagi/form.html', context)


@login_required
def edytuj_wpis(request, id):
    wpis = get_object_or_404(Rozciagi, pk=id)

    form = RozciagiForm(request.POST or None, request.FILES or None, instance=wpis)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_wpisy)

    context = {
        'form': form
    }

    return render(request, 'rozciagi/form.html', context)


@login_required
def usun_wpis(request, id):
    wpis = get_object_or_404(Rozciagi, pk=id)

    if request.method == 'POST':
        wpis.delete()
        return redirect(wszystkie_wpisy)

    context = {
        'wpis': wpis
    }
    return render(request, 'rozciagi/potwierdz.html', context)


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info( request, f"Witaj {username}! Właśnie się zalogowałeś.")
                return redirect("/")
            else:
                messages.error(request, f"Błędny login lub hasło")
        else:
            messages.error(request, f"- Błędny login lub hasło -")
    form = AuthenticationForm()

    context = {
        "form": form
    }
    return render(request, "rozciagi/login.html", context)


def logout_request(request):
    logout(request)
    messages.info(request, "Właśnie wylogowałeś się!")
    return redirect("/")


def is_valid_queryparam(param):
    return param != '' and param is not None



@login_required
def filtrowanie(request):
    qs = Rozciagi.objects.all()
    indeks_kontaktu_contains_query = request.GET.get('indeks_kontaktu_contains')
    numer_zlecenia_contains_query = request.GET.get('numer_zlecenia_contains')
    pracownik_contains_query = request.GET.get('pracownik_contains')
    narzedzia_contains_query = request.GET.get('narzedzia_contains')
    data_od = request.GET.get('data_od')
    data_do = request.GET.get('data_do')
    data_serwis_od = request.GET.get('data_serwis_od')
    data_serwis_do = request.GET.get('data_serwis_do')
    eksport = request.GET.get('eksport')

    if is_valid_queryparam(indeks_kontaktu_contains_query):
        qs = qs.filter(indeks_kontaktu__icontains = indeks_kontaktu_contains_query)

    elif is_valid_queryparam(numer_zlecenia_contains_query):
        qs = qs.filter(nr_zlecenia__icontains = numer_zlecenia_contains_query)

    elif is_valid_queryparam(pracownik_contains_query):
        qs = qs.filter(nr_pracownika = pracownik_contains_query)

    elif is_valid_queryparam(narzedzia_contains_query):
        qs = qs.filter(narzedzia = narzedzia_contains_query)

    if is_valid_queryparam(data_od):
        qs = qs.filter(data_dodania__gte = data_od + ' 00:00:00')

    if is_valid_queryparam(data_do):
        qs = qs.filter(data_dodania__lt = data_do + ' 23:59:59')

    if is_valid_queryparam(data_serwis_od):
        qs = qs.filter(data_serwis__gte = data_serwis_od + ' 00:00:00')

    if is_valid_queryparam(data_serwis_do):
        qs = qs.filter(data_serwis__lt = data_serwis_do + ' 23:59:59')

    if eksport == 'on':

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="eksport.csv"'
        response.write(u'\ufeff'.encode('utf8'))

        writer = csv.writer(response, dialect='excel', delimiter=';')
        writer.writerow(
            [
                'nr_zlecenia',
                'indeks_kontaktu',
                'poprawkowe',
                'nr_pozycji',
                'lista',
                'przekroj_przewodu',
                'rozciag',
                'wysokosc',
                'potwierdzenie',
                'nr_narzedzia',
                'narzedzia_rodzaj',
                'nr_pracownika',
                'grupa_robocza',
                'data_serwis',
                'data_dodania',
                'dział'
            ]
        )

        for obj in qs:
            writer.writerow(
                [
                    obj.nr_zlecenia,
                    obj.indeks_kontaktu,
                    obj.poprawkowe,
                    obj.nr_pozycji,
                    obj.lista,
                    obj.przekroj_przewodu,
                    obj.rozciag,
                    obj.wysokosc,
                    obj.potwierdzenie,
                    obj.narzedzia,
                    obj.narzedzia_rodzaj,
                    obj.nr_pracownika,
                    obj.grupa_robocza,
                    obj.data_serwis,
                    obj.data_dodania,
                    obj.zalogowany_user.dzial,
                ]
            )
        return response

    context = {
        'queryset': qs,
    }
    return render(request, 'rozciagi/filter.html', context)