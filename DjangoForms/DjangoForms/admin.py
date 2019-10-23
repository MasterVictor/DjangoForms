from django.contrib import admin
from .models import Pregunta, Respuesta, Usuario, Formulario, Detalle, AsigPregunta, AsigRespuesta
# Register your models here.

admin.site.register(Respuesta)
admin.site.register(Usuario)
admin.site.register(Pregunta)

class AsigPreguntaInline(admin.TabularInline):
    '''Tabular Inline View for Pregunta'''

    model = AsigPregunta
    extra = 1

class AsigRespuestaInline(admin.TabularInline):
    '''Tabular Inline View for Respuesta'''

    model = AsigRespuesta
    extra = 1


@admin.register(Formulario)
class FormularioAdmin(admin.ModelAdmin):
    '''Admin View for Formulario'''

    list_display = ('nombre','usuario')

    inlines = [
        AsigPreguntaInline,
    ]

@admin.register(Detalle)
class DetalleAdmin(admin.ModelAdmin):
    '''Admin View for Formulario'''

    #list_display = ('usua')

    inlines = [
        AsigRespuestaInline, 
    ]

