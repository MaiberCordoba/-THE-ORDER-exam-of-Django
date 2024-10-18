from rest_framework.routers import DefaultRouter
from apps.detallesPedidos.api.views import DetallePedidoModelView

router_detallesPedidos = DefaultRouter()

router_detallesPedidos.register(prefix="dtPedidos",basename="dtPedidos",viewset=DetallePedidoModelView)