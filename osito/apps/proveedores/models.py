from django.db import models
from apps.productos.models import Producto

# Create your models here.
class Proveedore(models.Model):
    nombre = models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    telefono = models.IntegerField(max_length=12)
    productos = models.ManyToManyField(Producto, through= 'Distribuidos')
    
    
 
    def __str__(self):
        return self.nombre


class Distribuidos(models.Model):
    proveedore = models.ForeignKey(Proveedore, on_delete =models.CASCADE,verbose_name="proveedor" )
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE,verbose_name="producto")
    cantidadProducto = models.IntegerField()     