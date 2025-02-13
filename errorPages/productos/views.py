from django.shortcuts import render,redirect
from .models import Producto
from django.http import JsonResponse
from .forms import productosForm 

# Create your views here.

#Vista que devuelve la lista de productos como json 

def lista_productos(request):
    #Obtener todos los productos de la base de datos 
    productos = Producto.objects.all()
    #guardar los datos lista de diccionarios
    #Este diccionario fue creado al aire y no es seguro
    data = [
        {
            "nombre": p.nombre,
            "precio": p.precio,
            "imagen": p.imagen
        }
        for p in productos
    ]
    return JsonResponse (data, safe=False)

def  ver_productos(request):
    return render(request, 'ver.html')

#vista que carge y maneje el formulario de productos
def agregar_producto(request):
    #cheaacr si vengo del formulario 

    if request.method == 'POST':
         # quiere decir que enviaron los form
        form = productosForm(request.POST)
        #cheacar si los datos estan bien 
        if form.is_valid():
            #lo guardo en la base de datos 
            form.save()
            return redirect('ver')
    #que pasa si no se mando el formulario
    else:
        #si el formulario no fue enviado
        form = productosForm()
    return render(request, 'agregar.html', {'form': form})