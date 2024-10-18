from django.db import models

# Create your models here.
class Configuracion (models.Model):
    nombre = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/')
    
    def _str_(self):
        return self.nombre