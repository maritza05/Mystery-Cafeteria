from django.db import models
from productos.models import Producto

class Inventario(models.Model):
	id_producto = models.ForeignKey(Producto)
	cantidad = models.IntegerField()

    def __unicode__(self):
        return u"Producto: " + str(self.id_producto) +" "+ self.cantidad