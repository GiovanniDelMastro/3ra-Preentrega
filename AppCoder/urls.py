from django.urls import path
from AppCoder.views import curso, listar_cursos
from .views import *
urlpatterns = [
    path('agrega-curso/<nombre>/<camada>',curso),
    path('lista-cursos/',listar_cursos),
    path('',inicio, name="Inicio"),
    path('cursos/',cursos, name="Cursos"),
    path('profesores/',profesores, name="Profesores"),
    path('entregables/',entregables, name="Entregables"),
    path('cursoFormularios/', cursoFormulario, name="cursoFormularios"),
    path('guardarProfesor/', guardarProfesor, name="guardarProfesor"),
    path('busqueda-curso/', busquedaCurso, name="busqueda-curso"),
    path('Buscando/', buscar, name="Buscando"),
    path('crearestudiante/', creaEstudiante, name="crearestudiante"),
    path('entregar-trabajo/', crear_entregable, name="entregar-trabajo"),

]
