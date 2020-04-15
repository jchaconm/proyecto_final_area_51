from django import forms
from django.contrib import admin
import requests

from clientes.models import Clientes

class NuevoClienteForm(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = ['nombre', 'apellido','dni','red_social','sexo']

    def clean(self):
        red_social_url = self.cleaned_data.get('red_social')
        try:
            req = requests.get(red_social_url)
            req.raise_for_status()
            if req.status_code != 200:
                raise forms.ValidationError("Red social no encontrada.Ingresar url valida")
        except:
            raise forms.ValidationError("Ingresar url valida")
        return self.cleaned_data


class NuevoClienteAdmin(admin.ModelAdmin):
    exclude = ['fecha_creacion', 'fecha_modificacion','creado_por']
    form = NuevoClienteForm

    def save_model(self, request, obj, form, change):
        obj.creado_por = request.user
        obj.save()