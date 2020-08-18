from django import forms
from django.core.exceptions import ValidationError


class CargaDatosPersonales(forms.Form):
    nombre_apellido = forms.CharField(max_length=200)
    edad = forms.IntegerField(max_value=120)

    def clean_nombre_apellido(self):
        nombre_apellido = self.cleaned_data['nombre_apellido']

        if "fisa" not in nombre_apellido:
            raise ValidationError("Solo fisa puede cargar sus datos")

        return nombre_apellido
