# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
        ('clientes', '0001_initial'),
        ('inventarios', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('total_venta', models.IntegerField()),
                ('atendido', models.BooleanField()),
                ('id_cliente', models.ForeignKey(to='clientes.Cliente')),
                ('id_empleado', models.ForeignKey(to='empleados.Empleado')),
                ('id_inventario', models.ForeignKey(to='inventarios.Inventario')),
                ('id_producto', models.ForeignKey(to='productos.Producto')),
            ],
        ),
    ]
