from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Plato
from .serializers import PlatoSerializer

@api_view(['GET'])
def obtener_platos_precio_mayor_igual_50(request):
    # Filtra los platos cuyo precio sea mayor o igual a 50 soles
    platos = Plato.objects.filter(precio__gte=50)
    # Serializa los paltos encontrados
    serializer = PlatoSerializer(platos, many=True)
    return Response(serializer.data)



