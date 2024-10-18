from django.db import models
from apps.pedidos.models import Pedidos
from apps.productos.models import Productos
# Create your models here.
class DetallePedido (models.Model):
    DetallesPedidos_choices=[
        ('llevar','llevar'),
        ('consumir','para consumo en el sitio')
    ]
    estado=models.CharField(max_length=30,choices=DetallesPedidos_choices,default='consumir')
    pedido = models.ForeignKey(Pedidos, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Productos, on_delete=models.SET_NULL,null=True )
    cantidad = models.PositiveIntegerField(default=1)
    observaciones = models.TextField()

    def __str__(self):
        return self.pedido.cliente