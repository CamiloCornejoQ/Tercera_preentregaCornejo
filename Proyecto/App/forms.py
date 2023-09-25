from django import forms
from .models import Compra, Producto, Cliente

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=200)

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)

class CompraForm(forms.Form):
    #cliente = forms.CharField(max_length=100)
    #producto = forms.CharField(max_length=100)
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), label='Producto',empty_label=None)
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), label='Cliente',empty_label=None)
    cantidad = forms.IntegerField()

class Meta:
        model = Compra
        fields = ['producto', 'cliente', 'cantidad']

class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(label='Término de búsqueda', max_length=255)