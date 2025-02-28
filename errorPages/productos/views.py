from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

class ProductViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    #como renderizar mis respuestas 

    render_classes = [JSONRenderer]
    #permitir filtrar que metodos HTTP se puedan usar
    #CRUD
    #http_method_names = 