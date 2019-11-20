from rest_framework import viewsets, filters
from .models import Formulario, Pregunta, Respuesta, AsigPregunta
from .serializers import FormularioSerializer, PreguntaSerializer, RespuestaSerializer, AsigPreguntaSerializer
# from ..users.models import profile
# from ..users.serializers import ProfileSerializer

class FormularioViewSet(viewsets.ModelViewSet):
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre','profile__user','profile__descripcion']

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer

class RespuestaViewSet(viewsets.ModelViewSet):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['respuesta','formulario__nombre']

class AsigPreguntaViewSet(viewsets.ModelViewSet):
    queryset = AsigPregunta.objects.all()
    serializer_class = AsigPreguntaSerializer

#     products = Product.objects.filter(store_set__in=stores_qs)
# stores_qs = Store.objects.filter(product__name='product_name')
