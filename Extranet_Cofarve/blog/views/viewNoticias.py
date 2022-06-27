from ..forms import PostGaleria
from ..models import Noticias
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.db import connection



def noticia(request): 
    noticia = Noticias.objects.all()

    contexto = {"noticia":noticia}
    return render(request, 'noticias.html', contexto) 


def updateNoticias(request, id):
    # nombre = request.POST['name']
    # descripcion = request.POST['description']
    enlace = request.POST['enlace']

    #nombre = 'admin'
    with connection.cursor() as cursor: 
        cursor.execute("UPDATE blog_Noticias SET enlace = '{enlace}' WHERE id = {id}".format(id=id, enlace=enlace))
        valor = cursor.fetchone()
        
    contexto = {'valor':valor}
    return render(request,'edit.html' , contexto)