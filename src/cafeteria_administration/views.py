from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def cafeteria(request):
	return render(request, 'cafeteria.html')
