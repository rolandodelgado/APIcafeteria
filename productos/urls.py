from django.urls import path, include
from rest_framework import routers
from .api import ProductosViewSet

router = routers.DefaultRouter()
router.register(r'productos', ProductosViewSet, basename='productos')


urlpatterns = router.urls