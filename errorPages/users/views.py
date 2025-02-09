from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomLoginForm  
import json
from .message import Message  # Corrección en la importación

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home')  
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomLoginForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)

    # Mensaje de cierre de sesión
    msg = Message("info", "Se ha cerrado la sesión correctamente", 200)

    # Opción 1: Renderizar login con mensaje
    return render(request, 'login.html', {'message': json.dumps(msg.to_dict())})

    # Opción 2 (mejor): Redirigir a login y pasar mensaje con Django messages
    # from django.contrib import messages
    # messages.info(request, "Se ha cerrado la sesión correctamente")
    # return redirect('login')

@login_required
def home_view(request):
    return render(request, 'home.html')
