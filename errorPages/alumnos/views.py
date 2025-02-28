from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Alumnos
from .serializers import AlumnoSerializer
# Create your views here.
class AlumnosViewset(viewsets.ModelViewSet):
    queryset = Alumnos.objects.all()
    serializer_class = AlumnoSerializer

    renderer_classes = [JSONRenderer]