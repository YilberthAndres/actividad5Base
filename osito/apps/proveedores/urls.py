from django.urls import path, include
from apps.proveedores.views import index

app_name = "proveedores"
urlpatterns = [
    path('',index)
]