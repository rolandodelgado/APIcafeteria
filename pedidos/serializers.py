# from rest_framework import serializers
# from .models import Pedido
# import json

# class PedidoSerializer(serializers.ModelSerializer):    
#     class Meta:
#         model = Pedido
#         fields = ['id', 'mesa', 'lista_productos', 'cliente','fecha_inicio', 'fecha_fin', 'estado']

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['lista_productos'] = json.loads(representation['lista_productos'])
#         return representation

from rest_framework import serializers
from .models import Pedido

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
        read_only_fields = ('id',)

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