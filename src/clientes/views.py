from django.shortcuts import render, redirect, get_object_or_404
from clientes.models import Cliente
from clientes.forms import ClientesForm



def listar(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista.html', {'clientes': clientes})


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

def consultar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'cliente/consultar_cliente.html', {'clientes':clientes})

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Clientes, pk=pk)
    cliente.delete()
    return redirect('listar')


def modificar_cliente(request, pk):
    return render(request, 'clientes/modificar_clientes.html', {'Clientes':cliente })
