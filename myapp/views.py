from django.shortcuts import render
from .models import Materia, Tema
from django.db.models import Q

# Create your views here.

def get_lista_materias():
    materias = Materia.objects.all()
    return materias

def get_lista_temas(busqueda=None):
    query = Tema.objects
    if busqueda:
        # query = query.filter(nombre__contains=busqueda)
        # query = query.filter(materia__nombre__contains=busqueda)
        query = query.filter(Q(materia__nombre__contains=busqueda) | Q(nombre__contains=busqueda))
    return query.all()

def lista_materia(request):
    template_name = 'materias-list.html'
    context = {
        'materias': get_lista_materias()
    }
    return render(request, template_name, context)

def lista_temas(request):
    template_name = 'temas-list.html'
    # TODO: create feature of search
    temas = []
    if request.GET:
        busqueda = request.GET['busqueda']
        if busqueda:
            temas = get_lista_temas(busqueda)
        else:
            temas = get_lista_temas()
        print('vamos a filtrar los temas por {}'.format(busqueda))
    else:
        temas = get_lista_temas()

    context = {
        'temas': temas
    }
    return render(request, template_name, context)