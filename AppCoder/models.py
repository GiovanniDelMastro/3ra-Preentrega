from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class estudiantes(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField

class Profesor(models.Model):
    nombre = models.CharField(max_length=43)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

class Entregable(models.Model):
    nombre = models.CharField(max_length=10)
    fechadeentrega = models.DateField()
    entregado = models.BooleanField()
    link = models.CharField(max_length=100, null=True)
