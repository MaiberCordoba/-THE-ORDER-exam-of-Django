from rest_framework.viewsets import ModelViewSet
from apps.detallesPedidos.models import DetallePedido
from apps.detallesPedidos.api.serializer import DetallePedidoSerializer

class DetallePedidoModelView(ModelViewSet):
    serializer_class = DetallePedidoSerializer
    queryset = DetallePedido.objects.all()