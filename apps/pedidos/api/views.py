from rest_framework.viewsets import ModelViewSet
from apps.pedidos.models import Pedidos
from apps.pedidos.api.serializer import PedidosSerializer

class PedidosModelView(ModelViewSet):
    serializer_class = PedidosSerializer
    queryset = Pedidos.objects.all()