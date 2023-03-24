from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Pedido
from .serializers import PedidoSerializer
from productos.models import Producto
from productos.serializers import ProductoSerializer


class PedidosViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    
    @action(detail=True, methods=['get'])
    def productos(self, request, pk=None):
        id_pedido = self.kwargs['pk']
        try:
            pedido = Pedido.objects.get(pk=id_pedido)
            lista_productos = []
            for producto_id in pedido.lista_productos:
                lista_productos.append(Producto.objects.get(pk=producto_id))
            return Response(ProductoSerializer(lista_productos, many=True).data, 
                            status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(None, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        