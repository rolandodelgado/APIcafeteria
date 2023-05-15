from rest_framework import serializers
from .models import Pedido
import json

class PedidoSerializer(serializers.ModelSerializer):
    lista_productos = serializers.SerializerMethodField()

    class Meta:
        model = Pedido
        fields = '__all__'
        read_only_fields = ('id',)

    def get_lista_productos(self, instance):
        lista_productos = instance.lista_productos
        formatted_json = json.dumps(lista_productos, indent=4)
        return formatted_json

    def create(self, validated_data):
        try:
            # id autoincremental
            last_pedido = Pedido.objects.order_by('-id').first()
            if last_pedido is None:
                validated_data['id'] = 1
            else:
                validated_data['id'] = last_pedido.id + 1

            return super().create(validated_data)
        except Exception as e:
           raise serializers.ValidationError("Failed to save the order")
