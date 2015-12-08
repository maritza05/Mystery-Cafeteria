from django.shortcuts import render, redirect, get_object_or_404
from puestos.models import Puesto
from puestos.forms import PuestoForm



def listar(request):
    puestos = Puesto.objects.all()
    return render(request, 'puestos/lista.html', {'puestos': puestos})


def nuevo_puesto(request):
    if request.method == "POST":
        form = PuestoForm(request.POST)
        if form.is_valid():
            puestos = form.save()
            puestos.save()
            return redirect('listar')
    else:
        form = PuestoForm()
    return render(request, 'puestos/nuevo_puesto.html', {'form': form, 'etiqueta_titulo': 'Agregar Puesto', 'etiqueta_boton': 'Agregar'})

def consulta_puesto(request, pk):
    puestos = get_object_or_404(Puesto, pk=pk)
    return render(request, 'puestos/consulta_puesto.html', {'puestos':puestos})

def eliminar_puesto(request, pk):
    puestos = get_object_or_404(Puesto, pk=pk)
    puestos.delete()
    return redirect('listar')


def modificar_puesto(request, pk):
    puestos = get_object_or_404(Puesto, pk=pk)
    if request.method == "POST":
        form = PuestoForm(request.POST, instance=puestos)
        if form.is_valid():
            puestos = form.save()
            puestos.save()
            return redirect('listar')
    else:
        form = PuestoForm(instance=puestos)
    return render(request, 'puestos/nuevo_puesto.html', {'form':form, 'etiqueta_titulo': 'Modificar Puesto', 'etiqueta_boton':'Actualizar'})
