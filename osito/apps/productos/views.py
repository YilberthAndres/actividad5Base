from django.http.response import HttpResponse
from django.shortcuts import render
from apps.productos.models import Producto
# Create your views here.
def index(request):   
    producto = Producto.objects.all().order_by('-id')
    context = {'productos': producto}
    return render(request, 'productos/index.html', context)