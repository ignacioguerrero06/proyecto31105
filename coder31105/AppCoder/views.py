from http.client import HTTPResponse
from django.shortcuts import render
from .models import Curso
# Create your views here.

def curso(request):
    curso=Curso(nombre='python',comision=31105)
    curso.save
    texto=f"Curso Creado: nombre:{curso.nombre} comision {curso.comision}"
    return HTTPResponse(texto)

