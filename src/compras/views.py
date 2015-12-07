from django.shortcuts import render, redirect, get_object_or_404
from compras.models import Compra
from compras.forms import CompraForm
from proveedores.models import Proveedor
from empleados.models import Empleado
from productos.models import Producto


def listar(request):
    compras = Compra.objects.all()
    return render(request, 'compras/lista.html', {'compras': compras})


def nueva_compra(request):
    if request.method == "POST":
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save()
            compra.save()
            return redirect('listar')
    else:
        form = CompraForm()
    return render(request, 'compras/nueva_compra.html', {'form': form, 'etiqueta_titulo': 'Realizar Nueva', 'etiqueta_boton': 'Realizar Compra'})


def eliminar_compra(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    compra.delete()
    return redirect('listar')


def detalles_compra(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    proveedor = get_object_or_404(Proveedor, compra.id_proveedor)
    empleado = get_object_or_404(Empleado, compra.id_empelado)
    return render(request, 'compras/detalles.html', {'compra':compra, 'proveedor':proveedor, 'empleado':empleado})


def menu_productos(request):
    productos = Producto.objects.all()
    print productos
    return render(request, 'compras/menu_productos.html', {'productos':productos})


def promociones(request):
    productos = Producto.objects.all()
    print productos
    return render(request, 'compras/promociones.html', {'productos':productos})
