from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from apps.proveedores.models import Proveedore

# Create your views here.

def index (request):

    proveedor = Proveedore.objects.all().order_by('id')
    context = {'proveedores' : proveedor}
    return render(request, 'proveedores/index.html', context)