from django.forms import ModelForm
from .models import Rozciagi, GrupaRobocza, Narzedzia
from django import forms


class RozciagiForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RozciagiForm, self).__init__(*args, **kwargs)
        self.fields['grupa_robocza'] = forms.ModelChoiceField(queryset=GrupaRobocza.objects.filter(aktywna=True))
        self.fields['narzedzia_rodzaj'] = forms.ModelChoiceField(queryset=Narzedzia.objects.filter(aktywny=True))

    class Meta:
        model = Rozciagi
        fields = [
            'nr_zlecenia',
            'nr_pozycji',
            'lista',
            'nr_pracownika',
            'grupa_robocza',
            'rozciag',
            'przekroj_przewodu',
            'indeks_kontaktu',
            'poprawkowe',
            'narzedzia',
            'narzedzia_rodzaj',
            'potwierdzenie',
            'wysokosc'
        ]