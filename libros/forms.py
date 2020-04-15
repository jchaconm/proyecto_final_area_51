import decimal

import requests
from bs4 import BeautifulSoup
from django import forms
from django.contrib import admin

from libros.models import Libros


class NuevoLibroForm(forms.ModelForm):

    class Meta:
        model = Libros
        fields = ['nombre', 'precio','stock']


class NuevoLibroAdmin(admin.ModelAdmin):
    exclude = ['fecha_creacion', 'fecha_modificacion','creado_por','precio_sin_igv','']
    readonly_fields = ['resumen','precio_dolar']
    form = NuevoLibroForm

    def save_model(self, request, obj, form, change):
        obj.creado_por = request.user
        obj.resumen = obtenerResumen(obj.nombre)
        obj.precio_dolar = obtenerPrecioDolar(obj.precio)
        obj.save()


def obtenerResumen(nombre):
    search_obj = nombre.replace(' ', '_')
    URL = f'https://es.wikipedia.org/wiki/{search_obj}'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    seccion_argumento = soup.find(id='Argumento')

    if not seccion_argumento:
        resumen = 'Resumen no disponible'
    else:
        contenido_argumento =  seccion_argumento.findNext('p').text
        if not contenido_argumento:
            # En caso no se encuentre el elemento con id argumento
            contenido_argumento = seccion_argumento.parent().findNext('p').text
        resumen = contenido_argumento
    return resumen

def obtenerPrecioDolar(precio):
    URL = f'http://data.fixer.io/api/latest?access_key=ce2c726b45001ac3884d897bf7d6f035'
    tasa_cambio_req = requests.get(URL)
    tasa_cambio_data = tasa_cambio_req.json()
    cambio_soles = decimal.Decimal(tasa_cambio_data['rates']['PEN'])

    return round(precio / cambio_soles, 2)
