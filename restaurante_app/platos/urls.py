from django.urls import path
from . import views

urlpatterns = [
    path('api/platos/precio-50/', views.obtener_platos_precio_mayor_igual_50, name='platos_precio_50'),
]
