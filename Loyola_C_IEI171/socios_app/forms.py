from django import forms
from socios_app.models import Socios
from django.forms import DateInput
from django.core.exceptions import ValidationError
from django.forms import CharField
import re

class FormSocio(forms.ModelForm):
    telefono = CharField(required=True)
    email = forms.EmailField(error_messages={'invalid': 'Ingresa un email válido.'})

    class Meta:
        model = Socios
        fields = '__all__'
        labels = {
            'nombreSocio': 'Nombre',
            'fechaIncorporacion': 'Fecha de Incorporación',
            'anoNacimiento': 'Año de Nacimiento',
            'telefono': 'Teléfono',
            'email': 'Correo Electrónico',
            'sexo': 'Sexo',
            'estado': 'Estado',
            'observacion': 'Observaciones',
        }
        widgets = {
            'fechaIncorporacion': DateInput(attrs={'type': 'date'}),
            'anoNacimiento': DateInput(attrs={'type': 'date'}),
            'email': forms.EmailInput(attrs={'type': 'email'}),
        }
    
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not re.match(r'^\+?1?\d{9,15}$', telefono):
            raise ValidationError('Ingresa un número de teléfono válido.')
        return telefono