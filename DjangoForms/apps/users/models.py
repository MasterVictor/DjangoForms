from django.contrib.auth.models import User
from django.db import models

#modelo de perfil
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True 
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def str(self):
        return self.user.username