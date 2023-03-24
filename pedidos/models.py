from djongo import models
from productos.models import Producto

class Pedido(models.Model):
    id = models.IntegerField(primary_key=True)
    productos = models.ArrayField(model_container=Producto)
    objects = models.DjongoManager()