from django.contrib import admin

# Register your models here.
from libros.forms import NuevoLibroAdmin
from libros.models import Libros

admin.site.register(Libros,NuevoLibroAdmin)
