from django.db import models
from categorias.models import Categoria
    
class DetallesProducto(models.Model):
    #relacion uno a uno
    descripcion = models.CharField(max_length=300)
    fecha_caducidad = models.DateField()

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)

# Create your models here.
#clase de productos 
class Producto(models.Model):
    #Atributos de la clase
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()
    detalles_producto = models.OneToOneField(DetallesProducto, on_delete=models.CASCADE, null=True, blank=True)
    Proveedor = models.ManyToManyField(Proveedor)
    Categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    #cuando se quiera utilizar una relacion se usa un campo:
    #OneToOneField (1 a 1)
    #ForeignKey (1 a muchos)
    #ManyToManyField (muchos a muchos)



    def __str__(self):
        return self.nombre
    
    #necesito una funcion que devuelva el objeto en fotma de dict
    def to_dict(self):
        return {
            #'clavevalor': 'valor'
            "nombre": self.nombre,
            "precio": self.precio,
            "imagen": self.imagen
        }
