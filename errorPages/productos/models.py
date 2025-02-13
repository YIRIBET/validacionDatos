from django.db import models

# Create your models here.
#clase de productos 
class Producto(models.Model):
    #Atributos de la clase
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()

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
    
