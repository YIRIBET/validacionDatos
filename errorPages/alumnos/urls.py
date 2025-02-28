from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AlumnosViewset, alumnos

# Configuración del router para la API de Alumnos
router = SimpleRouter()
router.register(r'api', AlumnosViewset)

urlpatterns = [
    # Rutas de la API de Alumnos
    path('', include(router.urls)),  # Esto incluye las rutas generadas automáticamente por el router
    
    # Ruta para la vista HTML que muestra los alumnos
    path('alumnos/', alumnos, name='alumnos'),  # Página de lista de alumnos
]
