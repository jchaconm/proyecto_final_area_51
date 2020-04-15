from django.contrib import admin

# Register your models here.
from ventas.forms import NuevoVentasAdmin
from ventas.models import Ventas

admin.site.register(Ventas,NuevoVentasAdmin)
