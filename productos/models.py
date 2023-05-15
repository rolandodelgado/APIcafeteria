from django.db import models
from djongo import models as djmodels

class Producto(models.Model):
    id = djmodels.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField(default=0) # Puede ser mas adecuado usar DecimalField
    activo = models.BooleanField(default=1)

    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.precio}'
