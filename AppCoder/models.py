from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    def __str__(self):
        return f'{self.nombre} - {self.camada}'
class estudiantes(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=100, default=[])
    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.email}'

class Profesor(models.Model):
    nombre = models.CharField(max_length=43)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.email} - {self.profesion}'

class Entregable(models.Model):
    nombre = models.CharField(max_length=10)
    fechadeentrega = models.DateField()
    entregado = models.BooleanField()
    link = models.CharField(max_length=100, null=True)
