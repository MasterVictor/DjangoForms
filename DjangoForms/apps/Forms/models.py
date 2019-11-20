from django.db import models
from users.models import Profile

# Create your models here.
from django.db import models

# Create your models here.


class Pregunta(models.Model):
    """Model definition for Preguntas."""
    PREGUNTA_CHOICES = [
        ("Texto", "Texto"),
        ("Opcion multiple", "Opcion multiple"),
        ("Verdadero y falso", "Verdadero y falso"),
    ]
    pregunta = models.TextField(primary_key=True)
    tipo = models.TextField(choices=PREGUNTA_CHOICES,null=True, blank=True)
    def __str__(self):
        """Unicode representation of Preguntas."""
        return self.pregunta

class Formulario(models.Model):
    """Model definition for Formulario."""
    nombre = models.TextField(primary_key=True)
    descripcion = models.TextField(null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Profile,on_delete=models.PROTECT, null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    pregunta = models.ManyToManyField(Pregunta, through="AsigPregunta")
    def __str__(self):
        """Unicode representation of Formulario."""
        return "Form: " + self.nombre + " From: " + str(self.user.descripcion)

class AsigPregunta(models.Model):
    """Model definition for AsigPregunta."""
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE)

class Respuesta(models.Model):
    """Model definition for Respuesta."""
    respuesta = models.TextField(primary_key=True, unique=False)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE)
    # formulario_pregunta = models.ForeignKey(AsigPregunta, on_delete=models.CASCADE)

    def __str__(self):
        """Unicode representation of Respuesta."""
        return "Respuesta: " + self.respuesta + " de: " + self.user.descripcion








