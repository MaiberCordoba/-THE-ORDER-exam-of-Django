from rest_framework.viewsets import ModelViewSet
from apps.factura.models import Factura
from apps.factura.api.serializer import FacturaSerializer

class FacturaModelView(ModelViewSet):
    serializer_class = FacturaSerializer
    queryset = Factura.objects.all()