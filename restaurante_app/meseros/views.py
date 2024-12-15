
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Mesero
from .serializers import MeseroSerializer

@api_view(['GET'])
def obtener_meseros_mayores_25(request):
    meseros = Mesero.objects.filter(edad__gt=25)  # Filtra a los meseros mayores de 25 años
    serializer = MeseroSerializer(meseros, many=True)
    return Response(serializer.data)


# meseros/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Mesero
from .forms import MeseroForm

# Vista para crear un mesero
class CrearMesero(CreateView):
    model = Mesero
    form_class = MeseroForm
    template_name = 'meseros/crear_mesero.html'  # Plantilla para la creación
    success_url = reverse_lazy('listar_meseros')  # Redirige a la lista de meseros

# Vista para listar meseros de procedencia Perú
class ListarMeserosPeru(ListView):
    model = Mesero
    template_name = 'meseros/listar_meseros_peru.html'  # Plantilla para listar
    context_object_name = 'meseros'

    def get_queryset(self):
        # Filtra los meseros cuya procedencia sea Perú
        return Mesero.objects.filter(procedencia='Perú')


# meseros/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import Mesero
from .forms import MeseroForm

class EditarMesero(UpdateView):
    model = Mesero
    form_class = MeseroForm
    template_name = 'meseros/editar_mesero.html'  # Especifica la plantilla correcta
    success_url = reverse_lazy('listar_meseros')  # Redirige a la lista de meseros después de editar


# meseros/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Mesero

class EliminarMesero(DeleteView):
    model = Mesero
    template_name = 'meseros/eliminar_mesero.html'  # Asegúrate de que esta plantilla exista
    success_url = reverse_lazy('listar_meseros')  # Redirige a la lista de meseros después de eliminar


from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Mesero

class ListarMeseros(ListView):
    model = Mesero
    template_name = 'meseros/listar_meseros.html'  # Plantilla que vamos a crear
    context_object_name = 'meseros'



# meseros/views.py
from django.views.generic import DetailView
from .models import Mesero

class VerDetalleMesero(DetailView):
    model = Mesero
    template_name = 'meseros/detalle_mesero.html'  # Plantilla para mostrar los detalles
    context_object_name = 'mesero'  # Esta es la variable que usaremos en la plantilla para acceder al mesero


# meseros/serializers.py
from rest_framework import serializers
from .models import Mesero

class MeseroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesero
        fields = '__all__'  # Incluir todos los campos del modelo Mesero

# meseros/views.py
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from .models import Mesero
from .serializers import MeseroSerializer

class CrearMeseroAPI(CreateAPIView):
    model = Mesero
    serializer_class = MeseroSerializer
    permission_classes = [IsAuthenticated]  # Solo los usuarios autenticados pueden crear meseros

