# Generated by Django 3.0.5 on 2020-04-15 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_clientes_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='red_social',
            field=models.CharField(max_length=100, verbose_name='URL de red social'),
        ),
    ]
