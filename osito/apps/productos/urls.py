from django.urls import path, include
from apps.productos.views import index
app_name = "productos"
urlpatterns = [
    path('', index)
]

