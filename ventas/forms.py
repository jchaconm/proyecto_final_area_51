from django import forms
from django.contrib import admin

from ventas.models import Ventas


class NuevaVentaForm(forms.ModelForm):

    class Meta:
        model = Ventas
        fields = ['libro', 'cliente','cantidad']

    def clean(self):
        cantidad = self.cleaned_data.get('cantidad')
        libro = self.cleaned_data.get('libro')
        if libro.stock - cantidad < 0:
            raise forms.ValidationError(f"Stock insuficiente para realizar la venta.Stock actual del producto:{libro.stock}")
        return self.cleaned_data

class NuevoVentasAdmin(admin.ModelAdmin):
    exclude = ['fecha_creacion', 'fecha_modificacion','creado_por','monto_igv']
    form = NuevaVentaForm

    def save_model(self, request, obj, form, change):
        #calculo precio
        precio_libro = obj.libro.precio
        porcentaje_igv = 18
        precio_sin_igv = lambda x: obj.cantidad * x

        #1 . declaracion de funcion de orden superior
        high_ord_func = lambda x, func: porcentaje_igv * func(x)

        obj.creado_por = request.user
        obj.monto_igv = high_ord_func(precio_libro, precio_sin_igv)
        obj.precio_sin_igv = precio_sin_igv(precio_libro)
        obj.save()

        #2- Actualizacion stock
        obj.libro.stock = obj.libro.stock - obj.cantidad
        obj.libro.save()

