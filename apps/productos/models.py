from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.TextField
    precio=models.DecimalField
    
    def __str__(self):
        return self.nombre
