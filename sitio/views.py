from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from sitio.models import Noticia
from datetime import datetime

from sitio.forms import CargaDatosPersonales



def inicio(request):
    # nueva = Noticia()
    # nueva.titulo = 'entro alguien!'
    # nueva.texto = 'acaba de entrar alguien al sitio'
    # nueva.fecha = datetime.now()
    # nueva.save()

    noticias = Noticia.objects.filter(archivada=False).order_by("fecha")
    return render(request, 'inicio.html', {'lista_noticias': noticias})


def ejemplo_form(request):
    if request.method == 'POST':
        # el usuario está mandando sus datos
        nombre_apellido = request.POST['nombre_apellido']
        edad = request.POST['edad']
    else:
        # el usuario está entrando a la página a ver el form
        nombre_apellido = '(todavía no se mandó)'
        edad = '(todavía no se mandó)'

    return render(request, "ejemplo_form.html", {
        'nombre_apellido': nombre_apellido,
        'edad': edad,
    })


def ejemplo_form_copado(request):
    if request.method == 'POST':
        # el usuario está mandando sus datos
        form_datos = CargaDatosPersonales(request.POST)

        if form_datos.is_valid():
            nombre_apellido = form_datos.cleaned_data['nombre_apellido']
            edad = form_datos.cleaned_data['edad']
            print("datos ingresados:", nombre_apellido, edad)

            return HttpResponseRedirect('/inicio')
    else:
        form_datos = CargaDatosPersonales()

    return render(request, "ejemplo_form_copado.html", {'form_datos': form_datos})


def ejemplo_ajax(request):
    return render(request, "ejemplo_ajax.html", {})


def publicidad_ajax(request):
    return render(request, "publicidad_ajax.html")


def cantidad_noticias_ajax(request):
    datos = {
        "cantidad_total": Noticia.objects.all().count(),
        "hay_archivadas": Noticia.objects.filter(archivada=True).exists()
    }

    return JsonResponse(datos)
