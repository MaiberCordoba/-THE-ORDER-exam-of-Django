from rest_framework.routers import DefaultRouter
from apps.configuracion.api.views import ConfiguracionModelView

router_configuracion = DefaultRouter()

router_configuracion.register(prefix="configuracion",basename="configuracion",viewset=ConfiguracionModelView)