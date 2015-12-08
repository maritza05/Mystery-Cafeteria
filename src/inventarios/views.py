from django.shortcuts import render
from inventarios.models import Inventario


def listar(request):
    inventarios = Inventario.objects.all()
    return render(request, 'inventarios/lista.html', {'inventarios': inventarios})
# Create your views here.
