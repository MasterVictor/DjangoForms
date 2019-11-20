from django.contrib import admin
from .models import Pregunta, Respuesta, Formulario, AsigPregunta

# Register your models here.
admin.site.register(Respuesta)
admin.site.register(Pregunta)
admin.site.register(AsigPregunta)

class AsigPreguntaInline(admin.TabularInline):
    '''Tabular Inline View for Pregunta'''

    model = AsigPregunta
    extra = 1


@admin.register(Formulario)
class FormularioAdmin(admin.ModelAdmin):
    '''Admin View for Formulario'''

    list_display = ('nombre','user')

    inlines = [
        AsigPreguntaInline,
    ]


