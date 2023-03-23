from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.response import Response
from pedidos.models import Pedidos
from .serializers import ProductoSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    # Minimamente hay que pasar queryset y serializer_class
    queryset = Pedidos.objects.all()
    serializer_class = ProductoSerializer