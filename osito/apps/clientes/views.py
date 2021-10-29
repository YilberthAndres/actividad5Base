from django.shortcuts import render
from django.http import HttpResponse
from apps.clientes.models import Cliente
# Create your views here.

def index(request):
    cliente = Cliente.objects.all().order_by('-id')
    context = {'clientes': cliente}
    return render(request, 'clientes/listar.html', context)
