from django.db import models
from djongo import models as djmodels

class Pedido(models.Model):
    ESTADOS = (
        ('Pedido', 'P'),
        ('Cocinando', 'C'),
        ('Listo', 'L'),
        ('Entregado', 'E'),
        ('Finalizado', 'F')
    )

    id = djmodels.IntegerField(primary_key=True)
    mesa = djmodels.IntegerField()
    lista_productos = djmodels.JSONField()
    cliente = djmodels.CharField(max_length=200)
    fecha_inicio = djmodels.DateTimeField(auto_now_add=True)
    fecha_fin = djmodels.DateTimeField(null=True)
    estado = djmodels.CharField(max_length=10, choices=ESTADOS, default='Pedido')
    total = djmodels.IntegerField()

    def __str__(self):
        return f"Pedido {self.id}"