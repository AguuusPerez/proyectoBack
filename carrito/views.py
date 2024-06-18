from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .carro import Carro
from catalogo.models import Producto
from django.contrib.auth.decorators import login_required


# Create your views here.
class Home(TemplateView):
    template_name = "carrito.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        carro = Carro(self.request)
        context['productos'] = carro.carro.values()
        context['total'] = carro.obtener_total()
        return context
    
@login_required
def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carro.agregar(producto=producto)
    return redirect("catalogo")

@login_required
def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("carrito")

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("carrito")