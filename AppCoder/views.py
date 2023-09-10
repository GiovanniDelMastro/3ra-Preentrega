from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *

# Create your views here.
def curso(req, nombre, camada):
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    return HttpResponse(f"""
    <p>Curso: {curso.nombre} - Camada: {curso.camada} creado con exito</p>
    """)

def listar_cursos(req):
    lista = Curso.objects.all()

    return render(req, "lista_cursos.html", {"lista_cursos": lista})

def inicio(req):
    return render(req,'inicio.html')

def cursos(req):
    return render(req,'cursos.html')

def profesores(req):
    return render(req,'profesores.html')

def estudiantes(req):
    return render(req,'estudiantes.html')

def entregables(req):
    return render(req,'entregables.html')

def cursoFormulario(req):
    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
        curso = Curso(nombre=req.POST["curso"], camada=req.POST["camada"])
        curso.save()
        return render(req, 'cursoguardado.html')
    else:
        return render(req, 'cursoFormulario.html')

def guardarProfesor(req):
    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':

        miFormulario = Profesorguardar(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            profesores = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"])
            profesores.save()
        return render(req, 'exitogprofesor.html.html')
    else:
        miFormulario = Profesorguardar(req.POST)
        return render(req, 'guardarprofesor.html', {"miformulario": miFormulario})    
    
def busquedaCurso(req):
    return render(req, "busquedacurso.hmtl")