from django.db import models

# Create your models here.
class alumnos(models.Model):
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    edad = models.IntegerField()
    documento = models.IntegerField()