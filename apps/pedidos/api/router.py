from rest_framework.routers import DefaultRouter
from apps.pedidos.api.views import PedidosModelView

router_pedidos = DefaultRouter()

router_pedidos.register(prefix="pedidos",basename="pedidos",viewset=PedidosModelView)