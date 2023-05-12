from django.db import models
from djongo import models as djmodels

class Pedido(models.Model):
    ESTADOS = (
        ('P', 'Pedido'),
        ('C', 'Cocina'),
        ('E', 'Entregado'),
        ('F', 'Finalizado')
    )

    id = djmodels.IntegerField(primary_key=True)
    mesa = djmodels.IntegerField()
    lista_productos = djmodels.JSONField()
    cliente = djmodels.CharField(max_length=200)
    fecha_inicio = djmodels.DateTimeField(auto_now_add=True)
    fecha_fin = djmodels.DateTimeField(null=True)
    estado = djmodels.CharField(max_length=1, choices=ESTADOS, default='P')

    def __str__(self):
        return f"Pedido {self.id}"