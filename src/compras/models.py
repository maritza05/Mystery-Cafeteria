# coding: utf-8 #
from django.db import models
from proveedores.models import Proveedor
from empleados.models import Empleado
from inventarios.models import Inventario


class Compra(models.Model):
    id_proveedor = models.ForeignKey(Proveedor)
    id_empleado = models.ForeignKey(Empleado)
    id_inventario = models.ForeignKey(Inventario)
    fecha = models.DateField()
    monto = models.IntegerField()

    def __unicode__(self):
        return u"Número de compra: [" + str(self.id) + "]"
