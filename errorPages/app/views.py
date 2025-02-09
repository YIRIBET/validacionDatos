from django.shortcuts import render
import requests
from django.conf import settings

from .models import *


from django.http import JsonResponse





GOOGLE_API_KEY = getattr(settings, "GOOGLE_API_KEY", "")
SEARCH_ENGINE_ID = getattr(settings, "SEARCH_ENGINE_ID", "")

def google_search(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": GOOGLE_API_KEY,
        "cx": SEARCH_ENGINE_ID
    }
    response = requests.get(url, params=params)
    return response.json()


def index(request):
    return render(request, 'index.html', status=200)

def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def error_500_view(request):
    return render(request, '500.html', status=500)

def one_page(request):
    return render(request, 'onePage.html', status=200)

def generar_error(request):
    return 7 / 0

def prueba_front(request):
    texto = request.GET.get('texto','')

    object1 = {
        'id':'001',
        'titulo':texto,
        'descripcion':'texto generico uno'
    }

    object2 = {
        'id': '002',
        'titulo': 'segundo titulo',
        'descripcion': 'texto generico uno'
    }

    object3 = {
        'id': '001',
        'titulo': 'tercer titulo',
        'descripcion': 'texto generico uno'
    }

    conjunto = [object1,object2,object3]


    #obtener datos en bd
    personas = Usuarios.objects.values('id','nombres','apellidos', 'edad')
    listaPersonas = list(personas)

    return render(
        request,
        'prueba.html',
        {'objeto':object1,
                'arreglo':conjunto,
                'lista':listaPersonas
         }

    )


def search_view(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        data = google_search(query)
        results = data.get("items", [])

    return render(request, "search.html", {"results": results, "query": query})



def error_logs(request):
    return render(request, 'error_logs.html')

def get_error_logs(request):
    errors = ErrorLog.objects.values('id', 'codigo', 'mensaje', 'fecha')
    return JsonResponse({'data': list(errors)})

