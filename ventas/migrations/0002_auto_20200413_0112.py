# Generated by Django 3.0.5 on 2020-04-13 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ventas',
            old_name='producto',
            new_name='libro',
        ),
        migrations.RemoveField(
            model_name='ventas',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='ventas',
            name='precio',
        ),
        migrations.AddField(
            model_name='ventas',
            name='creado_por',
            field=models.ForeignKey(max_length=15, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ventas',
            name='fecha_creacion',
            field=models.DateTimeField(default='2020-02-02', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ventas',
            name='fecha_modificacion',
            field=models.DateTimeField(default='2020-02-02', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ventas',
            name='precio_igv',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio'),
        ),
        migrations.AddField(
            model_name='ventas',
            name='precio_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio'),
        ),
    ]