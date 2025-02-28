from django.db import models

# Create your models here.
class Alumnos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    matricula = models.CharField(unique=True,max_length=19)
    correo = models.CharField(max_length=60,unique=True)

    def __str__(self):
        return self.nombre
    
    def to_dict(self):
        return{
            "nombre":self.nombre,
            "apellido":self.apellido,
            "edad":self.edad,
            "matricula":self.matricula,
            "correo":self.correo
        }