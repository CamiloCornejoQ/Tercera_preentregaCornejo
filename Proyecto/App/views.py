from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Cliente, Producto, Compra
from .forms import ClienteForm, ProductoForm, CompraForm,BusquedaForm

def inicio(request):
    return render(request,'App/inicio.html')

# Muestra informacion
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'App/cliente_list.html', {'clientes': clientes})

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'App/producto_list.html', {'productos': productos})

def compra_list(request):
    compras = Compra.objects.all()
    return render(request, 'App/compra_list.html', {'compras': compras})

# Formularios Cliente
def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        print(form)
        if form.is_valid():
            # Procesa los datos del formulario y guárdalos en la base de datos
            informacion= form.cleaned_data
            cliente = Cliente(nombre=informacion['nombre'], direccion=informacion['direccion'])
            cliente.save()
            return render(request, "App/inicio.html")
    else:
        form = ClienteForm()
    return render(request, 'App/cliente_form.html', {'form': form})

# Formularios Producto
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        print(form)
        if form.is_valid():
            # Procesa los datos del formulario y guárdalos en la base de datos
            producto = Producto(nombre=form.cleaned_data['nombre'], precio=form.cleaned_data['precio'])
            producto.save()
            return render(request, "App/inicio.html")
    else:
        form = ProductoForm()
    return render(request, 'App/producto_form.html', {'form': form})

# Formularios Compra
def compra_create(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        print(form)
        if form.is_valid():
            # Procesa los datos del formulario y guárdalos en la base de datos
            producto_id = form.cleaned_data['producto'].id
            cliente_id = form.cleaned_data['cliente'].id
            cantidad = form.cleaned_data['cantidad']
            nueva_compra = Compra.objects.create(
                producto_id=producto_id,
                cliente_id=cliente_id,
                cantidad=cantidad
            )
            return render(request, "App/inicio.html")
    else:
        form = CompraForm()
    return render(request, 'App/compra_form.html', {'form': form})

# Muestra informacion
def buscar(request):
    resultados_clientes = []
    resultados_productos = []
    resultados_compras = []

    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']

            # Realizar búsquedas en los modelos
            resultados_clientes = Cliente.objects.filter(nombre__icontains=termino_busqueda)
            resultados_productos = Producto.objects.filter(nombre__icontains=termino_busqueda)
            resultados_compras = Compra.objects.filter(cliente__nombre__icontains=termino_busqueda)

    else:
        form = BusquedaForm()

    return render(request, 'App/buscar.html', {
        'form': form,
        'resultados_clientes': resultados_clientes,
        'resultados_productos': resultados_productos,
        'resultados_compras': resultados_compras,
    })