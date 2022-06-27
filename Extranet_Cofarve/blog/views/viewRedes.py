
from ..forms import PostRedes
from ..models import RedeSociales
from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.shortcuts import render
from django.db import connection
from django.shortcuts import redirect
from django.utils.datastructures import MultiValueDictKeyError


def redes(request): 
    red = RedeSociales.objects.all()
    form = PostRedes() 
    if request.method == 'POST':
        form = PostRedes(request.POST) 
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            ser_instance = serializers.serialize('json', [ post, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)        
        
    else: 
        form = PostRedes() 

    contexto = {"red":red, "form":form}
    return render(request, 'redesSociales.html', contexto) 



def updateR(request, id):
    nombre = request.POST['name']
    icono = request.POST['icon']
    enlace = request.POST['enlace']
    try:
        estado = bool(request.POST['state'])
    except MultiValueDictKeyError:
        estado= False

    
    with connection.cursor() as cursor: 
        cursor.execute("UPDATE blog_RedeSociales SET name = '{name}', icon= '{icono}', enlace= '{enlace}', state= {estado} WHERE id = {id}".format(id=id, name=nombre, icono=icono, enlace = enlace ,  estado = estado))
        valor = cursor.fetchone()
        
    contexto = {'valor':valor}
    return render(request,'edit.html' , contexto)


def deleteRedes(request, pk):
    try:
        record = RedeSociales.objects.get(id = pk)
        record.delete()
        return redirect('RedesSociales')
    except:
        print("Record doesn't exists")