from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from empleados.models import Empleado
from empleados.forms import EmpleadoForm



def listar(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/lista.html', {'empleados': empleados})


def nuevo_empleado(request):
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            empleado = form.save()
            empleado.save()
            return redirect('listar')
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/nuevo_empleado.html', {'form': form, 'etiqueta_titulo': 'Agregar Empleado', 'etiqueta_boton': 'Agregar'})

def consulta_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    return render(request, 'empleados/consulta_empleado.html', {'empleado':empleado})

def eliminar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    empleado.delete()
    return redirect('listar')


def modificar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == "POST":
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            empleado = form.save()
            empleado.save()
            return redirect('listar')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleados/nuevo_empleado.html', {'form':form, 'etiqueta_titulo': 'Modificar Empleado', 'etiqueta_boton':'Actualizar'})
