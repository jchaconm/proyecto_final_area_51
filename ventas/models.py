from django.db import models

# Create your models here.
from clientes.models import Clientes, BaseModel
from libros.models import Libros


class Ventas(BaseModel):
    cantidad = models.PositiveIntegerField(verbose_name=u'Cantidad')
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, verbose_name=u'Cliente')
    libro = models.ForeignKey(Libros, on_delete=models.CASCADE, verbose_name=u'Producto')
    precio_sin_igv = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'Precio', default=0)
    monto_igv = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return str(self.nombre)

    class Meta:
     db_table = "ventas"