from djongo import models
from productos.models import Producto

class Pedidos(models.Model):
    mesa = models.IntegerField()
    productos = models.EmbeddedField(
        model_container = Producto
    )