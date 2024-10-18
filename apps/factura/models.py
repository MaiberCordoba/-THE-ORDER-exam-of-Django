from django.db import models
from apps.pedidos.models import Pedidos
# Create your models here.
class Factura (models.Model):
    pedido = models.ForeignKey(Pedidos,on_delete=models.SET_NULL,null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return self.pedido.cliente