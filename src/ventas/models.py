from django.db import models
from empleados.models import Empleado
from inventarios.models import Inventario
from clientes.models import Cliente
from productos.models import Producto

class Venta(models.Model):
	fecha = models.DateField()
	id_cliente = models.ForeignKey(Cliente)
	id_producto = models.ForeignKey(Producto)
	id_empleado = models.ForeignKey(Empleado)
	total_venta = models.IntegerField()
	atendido = models.BooleanField()
	id_inventario = models.ForeignKey(Inventario)
