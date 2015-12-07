from django.shortcuts import render, redirect, get_object_or_404
from compras.models import Compra
from compras.forms import CompraForm
from proveedores.models import Proveedor
from empleados.models import Empleado


def listar(request):
    compras = Compra.objects.all()
    return render(request, 'compras/lista.html', {'compras': compras})


def nuevo_cliente(request):
    if request.method == "POST":
        form = ClientesForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            cliente.save()
            return redirect('listar')
    else:
        form = ClientesForm()
    return render(request, 'clientes/nuevo_cliente.html', {'form': form, 'etiqueta_titulo': 'Agregar Cliente', 'etiqueta_boton': 'Agregar'})


def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Clientes, pk=pk)
    cliente.delete()
    return redirect('listar')


def modificar_compra(request, pk):
    return render(request, 'clientes/modificar_clientes.html', {'Clientes':cliente })
