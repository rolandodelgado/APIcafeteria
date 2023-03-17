from django.urls import path, include
from .views import productos

urlpatterns = [
    path('productos/', productos)
]