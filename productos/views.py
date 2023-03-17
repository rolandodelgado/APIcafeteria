from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Producto
import json

@csrf_exempt
def productos(request):
    respuesta = []
    if request.method == 'GET':
        productos = Producto.objects.all()
        for producto in productos:
            dict = {}
            dict['nombre'] = producto.nombre
            dict['precio'] = producto.precio
            respuesta.append(dict)
        return JsonResponse(respuesta, safe=False)
    elif request.method == 'POST':
        if request.content_type != 'application/json':
         return HttpResponse(status=400)
        try:
            json_data = json.loads(request.body.decode())
        except json.JSONDecodeError:
            return HttpResponse(status=400)
        
        producto = Producto(
            nombre = json_data.get('nombre', ''),
            precio = json_data.get('precio', '')
        )

        producto.save()
        return HttpResponse(status=201)