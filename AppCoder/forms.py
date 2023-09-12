from django import forms

class Profesorguardar(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=50)
    profesion = forms.CharField(max_length=20)
class Estudiantesguardar(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=50)
class GuardarEntregable(forms.Form):
    nombre = forms.CharField(max_length=10)
    fecha = forms.DateField()
    entregado = forms.BooleanField()
    link = forms.CharField(max_length=100)

