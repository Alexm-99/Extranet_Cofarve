from ..forms import PostTemas
from ..models import TemasImportantes
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.db import connection

def temasImportantes(request): 
    temas = TemasImportantes.objects.all()
    form = PostTemas()
    if request.method == 'POST': 
        if form.is_valid() :
            post = form.save(commit=False)
            post.save()
            ser_instance = serializers.serialize('json', [ post, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200) 

    else: 
        form = PostTemas() 

    contexto = {"temas":temas, "form":form}
    return render(request, 'temas.html', contexto) 



def updateT(request, id):
    nombre = request.POST['name']
    descripcion = request.POST['description']
    enlace = request.POST['enlace']

    #nombre = 'admin'
    with connection.cursor() as cursor: 
        cursor.execute("UPDATE blog_TemasImportantes SET name = '{name}', description= '{descripcion}', enlace = '{enlace}' WHERE id = {id}".format(id=id, name=nombre, descripcion=descripcion, enlace=enlace))
        valor = cursor.fetchone()
        
    contexto = {'valor':valor}
    return render(request,'edit.html' , contexto)