import json
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

# Función que agrega un producto con un objeto JSON
def registrar_producto(request):
    # Checar si nuestra request es de tipo POST
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parámetro es un texto que debería ser un JSON
            producto = Producto.objects.create(
                nombre=data['nombre'],
                precio=data['precio'],
                imagen=data['imagen']
            )
            # create directamente mete el objeto en la BD
            return JsonResponse(
                {
                    'mensaje': 'Registro exitoso',
                    'id': producto.id
                }, 
                status=201
            )
        except Exception as e:
            print(str(e))
            return JsonResponse({'error': str(e)}, status=400)

    # Si no es POST el request...
    return JsonResponse({'error': 'El método no está soportado'}, status=405)