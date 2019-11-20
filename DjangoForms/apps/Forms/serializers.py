from rest_framework import serializers
from .models import Formulario, Pregunta, Respuesta, AsigPregunta

class FormularioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulario
        fields = '__all__'

class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = '__all__'

class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = '__all__'

class AsigPreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsigPregunta
        fields = '__all__'    
