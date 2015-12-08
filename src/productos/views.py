from django.shortcuts import render, redirect, get_object_or_404
from productos.models import Producto
from productos.forms import ProductoForm


# Create your views here.
def listaproductos(request):
    productos = Productos.objects.all()
    return render(request, 'productos/lista.html', {'productos':productos})

def nuevo_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        print request.POST
        if form.is_valid():
            productos = form.save()
            productos.save()
            return redirect('listaproductos')
    else:
        form = ProductoForm
    return render(request, 'productos/nuevo_producto.html',{'form':form, 'etiqueta_titulo': 'Nuevo Producto','etiqueta_boton':'Nuevo'})

def eliminar_producto(request, pk):
    productos = get_object_or_404(Productos, pk=pk)
    productos.delete()
    return redirect('listaproductos')

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=productos)
        if form.is_valid():
            producto = form.save()
            producto.save()
            return redirect('listaproductos')
    else:
        form = ProductoForm(instance=productos)
    return render(request, 'productos/nuevo_producto.html',{'form':form,'etiqueta_titulo': 'Editar Producto', 'etiqueta':'Editar'})
