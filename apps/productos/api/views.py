from rest_framework.viewsets import ModelViewSet
from apps.productos.models import Productos
from apps.productos.api.serializer import ProductosSerializer

class ProductosModelView(ModelViewSet):
    serializer_class = ProductosSerializer
    queryset = Productos.objects.all()