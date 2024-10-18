from rest_framework.viewsets import ModelViewSet
from apps.configuracion.models import Configuracion
from apps.configuracion.api.serializer import ConfiguracionSerializer

class ConfiguracionModelView(ModelViewSet):
    serializer_class = ConfiguracionSerializer
    queryset = Configuracion.objects.all()