from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer
from django.shortcuts import render
from .forms import productosForm


def agregar_view(request):
    form = productosForm()
    return render (request, 'agregar.html',{'form':form})

    

class ProductViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    #como renderizar mis respuestas 
    render_classes = [JSONRenderer]
    #permitir filtrar que metodos HTTP se puedan usar
    #CRUD
    #http_method_names = 