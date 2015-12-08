from django.shortcuts import render
from inventarios.models import Inventario


def listar(request):
    inventarios = Inventario.objects.all()
    return render(request, 'inventarios/lista.html', {'inventarios': inventarios})

def modificar_inventario(request, pk):
    inventarios = get_object_or_404(Inventario, pk=pk)
    if request.method == "POST":
        form = InventarioForm(request.POST, instance=inventarios)
        if form.is_valid():
            inventarios = form.save()
            inventarios.save()
            return redirect('listar')
    else:
        form = InventarioForm(instance=inventarios)
    return render(request, 'inventarios/modificar_inventario.html', {'form':form, 'etiqueta_titulo': 'Modificar Inventario', 'etiqueta_boton':'Modificar'})
# Create your views here.
