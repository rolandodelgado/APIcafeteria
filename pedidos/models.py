from djongo import models

class Pedido(models.Model):
    id = models.IntegerField(primary_key=True)
    lista_productos = models.JSONField()
    objects = models.DjongoManager()