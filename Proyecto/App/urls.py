from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio,name="Inicio"),
    path('Clientes', views.cliente_list, name='cliente_list'),
    path('Productos', views.producto_list, name='producto_list'),
    path('compras', views.compra_list, name='compra_list'),
    path('clientes/crear/', views.cliente_create, name='cliente_create'),
    path('productocreate', views.producto_create, name='producto_create'),
    path('compracreate', views.compra_create, name='compra_create'),
    path('buscar/', views.buscar, name='buscar'),]