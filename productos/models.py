from djongo import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField(default=0) # Puede ser mas adecuado usar DecimalField

    class Meta:
        abstract = True