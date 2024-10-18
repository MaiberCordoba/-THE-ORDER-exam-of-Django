"""
URL configuration for The_Order project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from apps.productos.api.router import router_productos
from apps.pedidos.api.router import router_pedidos 
from apps.detallesPedidos.api.router import router_detallesPedidos 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router_productos.urls)),
    path('api/',include(router_pedidos.urls)),
    path('api/',include(router_detallesPedidos.urls)),

]
