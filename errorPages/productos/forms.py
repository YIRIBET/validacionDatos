#Generar todos los formularios html que vamos a ocupar 

from django import forms
from .models import Producto

#Crear una clase para cada ofrmnulario que necesitemos 
class productosForm(forms.ModelForm):
    class Meta:
        model = Producto
        #campos que se van a mostrar en el formulario
        fields = ['nombre', 'precio', 'imagen']
        #Etiquetas 
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio (MXN)',
            'imagen': 'URL de la imagen'
        }
        #personalizar mis campos
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del producto'
                }
            ),
            'precio': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el precio del producto'
                }
            ),
            'imagen': forms.URLInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la URL de la imagen'
                }
            )
        }

    #mensajes de error personalizados
    error_messages = {
        'precio':{
            'required': 'El precio no puede estar vacío',
            'invalid': 'Ingrese un precio válido'
        },
        'nombre':{
            'required': 'El nombre no puede estar vacío'
        },
    }