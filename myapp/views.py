from django.shortcuts import render
from .models import Materia
# Create your views here.

def get_lista_materias():
    materias = Materia.objects.all()
    return materias

def lista_materia(request):
    template_name = 'materias-list.html'
    context = {
        'materias': get_lista_materias()
    }
    return render(request, template_name, context)