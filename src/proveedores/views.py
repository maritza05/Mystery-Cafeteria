from django.shortcuts import render, redirect, get_object_or_404
from proveedores.models import Proveedor
from proveedores.forms import ProveedorForm


def listar(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/lista.html', {'proveedores': proveedores})


def nuevo_proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            proveedor = form.save()
            proveedor.save()
            return redirect('listar')
    else:
        form = ProveedorForm
    return render(request, 'proveedores/nuevo_proveedor.html', {'form': form, 'etiqueta': 'Nuevo', 'etiqueta_boton': 'Guardar proveedor'})


def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    proveedor.delete()
    return redirect('listar')


def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            proveedor = form.save()
            proveedor.save()
            return redirect('listar')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'proveedores/nuevo_proveedor.html', {'form': form, 'etiqueta': 'Actualizar', 'etiqueta_boton': 'Modificar proveedor'})
