from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Pedido
from productos.models import Producto
from .serializers import PedidoSerializer

class PedidosViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    
    @action(detail=True, methods=['get'])
    def productos(self, request, pk=None):
        id_producto = self.kwargs['pk']
        print("id_producto", id_producto)
        pedido = Pedido.objects.get(pk=id_producto)
        return Response(pedido.productos, status=status.HTTP_200_OK)
        