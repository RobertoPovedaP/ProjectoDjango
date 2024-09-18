from django.db import models

# Create your models here
class Tarea(models.Model):
    descripcion=models.CharField(max_length=255)
    completada=models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion