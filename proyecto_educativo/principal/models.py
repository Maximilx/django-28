from django.db import models

# Create your models here.
class Estudiantes(models.Model):
    nombre  = models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    correo  = models.EmailField(unique=True)
    edad    = models.IntegerField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
