from django.contrib import admin
from apps.proveedores.models import Proveedore, Distribuidos

# Register your models here.

class MembershipInline(admin.TabularInline):
    '''Tabular Inline View for '''

    model = Distribuidos
    
    extra = 1
class ProveedoresAdmin(admin.ModelAdmin) :
      inlines = (MembershipInline,)
      list_display = ('nombre', 'apellido', 'direccion', 'provincia', 'telefono')
      ordering = ('nombre', 'apellido', 'direccion', 'provincia', 'telefono')
      search_fields = ('nombre', 'apellido', 'direccion', 'provincia', 'telefono')




admin.site.register(Proveedore, ProveedoresAdmin)