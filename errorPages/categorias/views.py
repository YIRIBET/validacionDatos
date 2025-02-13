from django.shortcuts import render,redirect
from .models import Categoria
from django.http import JsonResponse
from .forms import CategoriaForm 

# Create your views here.

def lista_categoria(request):
    categorias = Categoria.objects.all()
    data = [
        {
            "nombre": c.nombre,
            "imagen": c.imagen
        }
        for c in categorias
    ]
    return JsonResponse(data, safe=False)

def ver_categoria(request):
    return render(request, 'verCategoria.html')

def registrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('verCategoria')
    else:
        form = CategoriaForm()
    return render(request, 'registrarCategoria.html', {'form': form})