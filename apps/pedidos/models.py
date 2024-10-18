from django.db import models
from apps.productos.models import Productos
# Create your models here.
class Pedidos(models.Model):
    pedidos_choices=[
        ('espera','espera'),
        ('preparacion','preparacion'),
        ('terminado','terminado')
    ]
    cliente=models.CharField(max_length=50)
    productos = models.ManyToManyField(Productos, through='detallesPedidos.DetallePedido')
    estado=models.CharField(max_length=30,choices=pedidos_choices,default='espera')
    
    def __str__(self):
        return self.cliente