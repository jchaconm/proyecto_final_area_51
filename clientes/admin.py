from django.contrib import admin

# Register your models here.
from clientes.forms import NuevoClienteAdmin
from clientes.models import Clientes

admin.site.register(Clientes,NuevoClienteAdmin)
