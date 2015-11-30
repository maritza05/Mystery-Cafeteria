from django.db import models

class Puesto (models.Model):
    puesto = models.CharField(max_length = 65)

    def __str__(self):
        return self.puesto
