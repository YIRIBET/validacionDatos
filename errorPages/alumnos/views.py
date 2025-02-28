from django.shortcuts import redirect, render
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Alumnos
from .serializers import AlumnoSerializer
from .forms import AlumnoForm

# Create your views here.
class AlumnosViewset(viewsets.ModelViewSet):
    queryset = Alumnos.objects.all()
    serializer_class = AlumnoSerializer

    renderer_classes = [JSONRenderer]

def alumnos(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.save()  # Guarda el nuevo alumno en la base de datos
            return redirect('alumnos')  # Redirige a la página de la lista de alumnos
    else:
        form = AlumnoForm()  # Si es GET, muestra el formulario vacío

    alumnos_list = Alumnos.objects.all()  # Recupera todos los alumnos
    return render(request, 'Rosel_Ilce.html', {'form': form, 'alumnos': alumnos_list})