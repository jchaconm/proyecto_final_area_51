
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    fecha_creacion = models.DateTimeField(max_length=20)
    fecha_modificacion = models.DateTimeField(max_length=20)
    creado_por = models.ForeignKey(User,max_length=15,on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.fecha_creacion = timezone.localtime(timezone.now())
        self.fecha_modificacion = timezone.localtime(timezone.now())
        super(BaseModel, self).save(*args, **kwargs)  # Call the "real" save() method.


class Clientes(BaseModel):

    SEX = [
        ("M","Masculino"),
        ("F","Femenino")
    ]

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=20)
    red_social = models.CharField(max_length=100,verbose_name="URL de red social")
    sexo = models.CharField(max_length=1, choices=SEX)


    class Meta:
     db_table = "clientes"

    def __str__(self):
        return f'{self.nombre} {self.apellido}'