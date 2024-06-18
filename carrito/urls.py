from django.urls import path
from carrito.views import Home, agregar_producto, eliminar_producto, restar_producto, limpiar_carro

urlpatterns = [
    path('', Home.as_view(), name='carrito'),
    path('agregar/<int:producto_id>/', agregar_producto, name='agregar_producto'),
    path('eliminar/int:<producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('restar/<int:producto_id>/', restar_producto, name='restar_producto'),
    path('limpiar/', limpiar_carro, name='limpiar_carro'),    
]