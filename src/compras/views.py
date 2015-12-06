from django.shortcuts import render
from compras.models import Compra


def listar(request):
    compras = Compra.objects.all()
    return render(request, 'compras/lista.html', {'compras': compras})
