from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model):
    user = models.OneToOneField(User, to_field="id", on_delete=models.CASCADE,blank=True, null=True, related_name="avatar")
    imagen = models.ImageField(upload_to="avatares", blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"