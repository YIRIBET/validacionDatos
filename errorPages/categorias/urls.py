from django.urls import path
from .views import * 

urlpatterns = [
    path('api/get/', lista_categoria,name = 'lista'),
    path('json/', ver_categoria, name = 'verCategoria'),
    path('registrar/', registrar_categoria, name = 'registrar'),
]