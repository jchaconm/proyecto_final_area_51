import requests
from bs4 import BeautifulSoup
from django.db import models

# Create your models here.
from clientes.models import BaseModel


class Libros(BaseModel):
    nombre = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'Precio')
    resumen = models.CharField(max_length=3000)
    stock = models.PositiveIntegerField(verbose_name='Cantidad disponible')
    class Meta:
     db_table = "libros"

    def save(self, *args, **kwargs):
        search_obj = self.nombre.replace(' ', '_')
        URL = f'https://es.wikipedia.org/wiki/{search_obj}'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        seccion_argumento = soup.find(id='Argumento')

        if not seccion_argumento:
            self.resumen = 'Resumen no disponible'
        else:
            if not (contenido_argumento := seccion_argumento.findNext('p').text):
                contenido_argumento = seccion_argumento.parent().findNext('p').text
            self.resumen = contenido_argumento
        return super(Libros, self).save(*args, **kwargs)  # Call the "real" save() method.
