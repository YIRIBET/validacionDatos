from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from .models import CustomUser
import re

# Formulario de Registro
class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'title': 'Ingresa una contraseña segura',
            'required': True
        })
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar Contraseña',
            'title': 'Repite la contraseña',
            'required': True
        })
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'required': True,
                'pattern': '^[a-zA-Z0-9._%+-]+@utez\.edu\.mx$',
                'title': 'Debes ingresar un correo válido de la UTEZ'
            }),
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'control_number': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'pattern': '^[0-9]{5}[a-zA-Z]{2}[0-9]{3}$',
                'title': 'La matrícula no pertenece a la UTEZ',
                'maxlength': '20'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': True,
                'title': 'Debes ser mayor de edad para registrarte',
                'max': '100',
                'min': '1'
            }),
            'tel': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
                
                'title': 'El número de teléfono debe tener exactamente 10 dígitos',
                'maxlength': '15'
            }),
        }

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if not re.match(r"^(?=.*\d)(?=.*[!#$%&?])(?=.*[a-zA-Z]).{8,}$", password):
            raise forms.ValidationError(
                "La contraseña debe tener al menos 8 caracteres, incluir al menos un número y un símbolo (!, #, $, %, & o ?)"
            )
        return password

    def clean_control_number(self):
        control_number = self.cleaned_data.get("control_number")
        if not re.match(r"^\d{5}[a-zA-Z]{2}\d{3}$", control_number):
            raise forms.ValidationError("La matrícula debe tener 10 caracteres en el formato correcto.")
        return control_number

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < 18:
            raise forms.ValidationError("Debes ser mayor de edad para registrarte.")
        return age

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

# Formulario de Inicio de Sesión
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("username")  
        password = cleaned_data.get("password")

        if email and password:
            user = authenticate(username=email, password=password) 
            if not user:
                raise forms.ValidationError("Usuario o contraseña incorrectos.")
        return cleaned_data
