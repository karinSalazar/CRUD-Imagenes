from django import forms
from .models import Automovil


class AutomovilForm(forms.ModelForm):
    class Meta:
        model = Automovil
        fields = ['patente', 'modelo', 'anio', 'marca', 'imagen']


