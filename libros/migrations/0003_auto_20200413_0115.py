# Generated by Django 3.0.5 on 2020-04-13 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_auto_20200413_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio'),
        ),
    ]