from django.db import models
from apps.proyecto.models import Proyecto
from apps.ecorregion.models import Ecorregion

class Registro(models.Model):
    especie = models.CharField(max_length=50)
    familia = models.CharField(max_length=50)
    nombrecomun = models.CharField(max_length=50)
    proyecto = models.ManyToManyField(Proyecto)
    baseregistro = models.TextField()
    identificador = models.CharField(max_length=50)
    añoidentificacion = models.CharField(max_length=50)
    departamento = models.CharField(max_length=20)
    municipio = models.CharField(max_length=20)
    localidad = models.CharField(max_length=20)
    latitud = models.FloatField()
    longitud = models.FloatField()
    autor = models.CharField(max_length=20)
    fechacaptura = models.DateField()
    ecorregion = models.ManyToManyField(Ecorregion)
