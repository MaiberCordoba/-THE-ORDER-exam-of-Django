from rest_framework.routers import DefaultRouter
from apps.factura.api.views import FacturaModelView

router_factura = DefaultRouter()

router_factura.register(prefix="factura",basename="factura",viewset=FacturaModelView)