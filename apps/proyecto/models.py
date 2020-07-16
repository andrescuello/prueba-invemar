from django.db import models


class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    informacion = models.TextField()

    def __str__(self):
        return self.nombre