from django.db import models


class Proveedor(models.Model):
    organizacion = models.CharField(max_length=65)
    email = models.EmailField()
    numero_telefono = models.CharField(max_length=10)

    def __unicode__(self):
        return self.organizacion
