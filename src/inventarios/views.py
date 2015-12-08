from django.shortcuts import render
from inventarios.models import Inventario


def listar(request):
    inventarios = Inventario.objects.all()
    return render(request, 'inventarios/lista.html', {'inventarios': inventarios})

def modificar_inventario(request, pk):
    inventarios = get_object_or_404(Inventario, pk=pk)
    if request.method == "POST":
        form = PuestoForm(request.POST, instance=puestos)
        if form.is_valid():
            puestos = form.save()
            puestos.save()
            return redirect('listar')
    else:
        form = PuestoForm(instance=puestos)
    return render(request, 'puestos/nuevo_puesto.html', {'form':form, 'etiqueta_titulo': 'Modificar Puesto', 'etiqueta_boton':'Actualizar'})
# Create your views here.
