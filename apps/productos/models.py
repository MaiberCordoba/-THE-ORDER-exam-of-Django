from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.TextField(max_length=255)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
  
    def __str__(self):
        return self.nombre
