from django.db import models

# Create your models here.

class Usuario(models.Model):
    """Model definition for Usuario."""
    nombre = models.TextField()
    nick = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField(max_length=254)
    contrasena = models.CharField(max_length=50)
    contracheck = models.CharField(max_length=50)
    is_creator = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    def __str__(self):
        """Unicode representation of Usuario."""
        return self.nick

    def get_absolute_url(self):
        return u'/aplicacion/usuario/'  

class Pregunta(models.Model):
    """Model definition for Preguntas."""
    PREGUNTA_CHOICES = [
        ("Texto", "Texto"),
        ("Opcion multiple", "Opcion multiple"),
        ("Verdadero y falso", "Verdadero y falso"),
    ]
    pregunta = models.TextField(null=True, blank=True)
    tipo = models.TextField(choices=PREGUNTA_CHOICES,null=True, blank=True)
    def __str__(self):
        """Unicode representation of Preguntas."""
        return self.pregunta

class Formulario(models.Model):
    """Model definition for Formulario."""
    nombre = models.TextField()
    descripcion = models.TextField(null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario,on_delete=models.PROTECT)
    link = models.TextField(null=True, blank=True)
    pregunta = models.ManyToManyField(Pregunta, through="AsigPregunta")
    def __str__(self):
        """Unicode representation of Formulario."""
        return "Form: " + self.nombre + " From: " + str(self.usuario)

class Respuesta(models.Model):
    """Model definition for Respuesta."""
    respuesta = models.TextField()
    def __str__(self):
        """Unicode representation of Respuesta."""
        return self.respuesta

class Detalle(models.Model):
    """Model definition for Detalle."""
    usuario = models.ForeignKey(Usuario,on_delete=models.PROTECT)
    formulario = models.ForeignKey(Formulario,on_delete=models.PROTECT)
    #fecha = models.DateTimeField(auto_now_add=True)
    respuesta=models.ManyToManyField(Respuesta, through="AsigRespuesta")
    def __str__(self):
        """Unicode representation of Detalle."""
        return "Resp de: " + str(self.usuario) + " del formulario: " + str(self.formulario)

class AsigPregunta(models.Model):
    """Model definition for AsigPregunta."""
    pregunta = models.ForeignKey(Pregunta, on_delete=models.PROTECT)
    formulario = models.ForeignKey(Formulario, on_delete=models.PROTECT)

class AsigRespuesta(models.Model):
    """Model definition for AsigPregunta."""
    respuesta = models.ForeignKey(Respuesta, on_delete=models.PROTECT)
    detalle = models.ForeignKey(Detalle, on_delete=models.PROTECT)



