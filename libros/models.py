import requests
from bs4 import BeautifulSoup
from django.db import models

# Create your models here.
from clientes.models import BaseModel

class Libros(BaseModel):
    nombre = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'Precio')
    precio_dolar = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'Precio Dólar')
    resumen = models.CharField(max_length=3000)
    stock = models.PositiveIntegerField(verbose_name='Cantidad disponible')
    class Meta:
     db_table = "libros"

    def __str__(self):
      return f'{self.nombre}'
