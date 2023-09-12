from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpRequest
from .forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView


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
        return render(req, 'exitogprofesor.html')
    else:
        miFormulario = Profesorguardar(req.POST)
        return render(req, 'guardarprofesor.html', {"miformulario": miFormulario})    
    
def busquedaCurso(req):
    return render(req, "busquedacurso.html")

def buscar(req: HttpRequest):
    camada = req.GET.get("camada", None)
    if camada:
        try:
            curso = Curso.objects.get(camada=camada)
            return render(req, 'resultadobusqueda.html', {"curso": curso})
        except Curso.DoesNotExist:
            return render(req,'nocamada.html')
    else:
        return HttpResponse('Debe agregar un parámetro "camada" en la URL')
    
def creaEstudiante(req):
    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':

        miFormulario2 = Estudiantesguardar(req.POST)
        if miFormulario2.is_valid():
            data = miFormulario2.cleaned_data
            estudiante = estudiantes(nombre=data["nombre"], apellido=data["apellido"], email=data["email"])
            estudiante.save()
        return render(req, 'estudianteguardado.html')
    else:
        miFormulario2 = Estudiantesguardar(req.POST)
        return render(req, 'crearestudiante.html', {"miformulario2": miFormulario2})  
     
def crear_entregable(req):
    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
        miFormulario2 = GuardarEntregable(req.POST)
        if miFormulario2.is_valid():
            data = miFormulario2.cleaned_data
            entregable = Entregable(nombre=data["nombre"], fecha=data["fecha"], email=data["email"], entregado=data["entregado"], link=data["link"])
            entregable.save()
        return render(req, 'Entregado.html')
    else:
        miFormulario2 = GuardarEntregable(req.POST)
        return render(req, 'creaentregable.html', {"miformulario2": miFormulario2}) 
        



