from django import forms

class Profesorguardar(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=50)
    profesion = forms.CharField(max_length=20)
