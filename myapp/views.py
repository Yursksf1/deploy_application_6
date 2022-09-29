from django.shortcuts import render
from .models import Materia, Tema
# Create your views here.

def get_lista_materias():
    materias = Materia.objects.all()
    return materias

def get_lista_temas():
    temas = Tema.objects.all()
    return temas

def lista_materia(request):
    template_name = 'materias-list.html'
    context = {
        'materias': get_lista_materias()
    }
    return render(request, template_name, context)

def lista_temas(request):
    template_name = 'temas-list.html'
    context = {
        'temas': get_lista_temas()
    }
    return render(request, template_name, context)