from django.shortcuts import render
from .models import Materia, Tema
from django.db.models import Q

# Create your views here.

def get_lista_materias(busqueda=None):
    query = Materia.objects
    if busqueda:
        query = query.filter(nombre__contains=busqueda)

    return query.all()

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

def materia_detalle(request):
    template_name = 'detalle-materia.html'

    materia = get_lista_materias()
    if request.GET and request.GET['materia_name']:
        materia_name = request.GET['materia_name']
        materia = get_lista_materias(materia_name)

    materia = materia[0]
    context = {
        'materia': materia,
        'temas': materia.tema_set.all()
    }
    return render(request, template_name, context)

def tema_detalle(request):
    template_name = 'detalle-tema.html'
    tema = get_lista_temas()
    if request.GET and request.GET['busqueda']:
        tema_name = request.GET['busqueda']
        tema = get_lista_temas(tema_name)

    if request.POST and request.POST.get('prueba'):
        prueba = request.POST.get('prueba')
        tema_name = request.GET['busqueda']
        tema = get_lista_temas(tema_name)
        tema[0].descripcion = prueba
        tema[0].save()

    context = {
        "tema": tema[0]
    }
    # your code is here
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