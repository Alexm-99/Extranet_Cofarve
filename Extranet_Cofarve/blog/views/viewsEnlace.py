from ..models import *
from django.shortcuts import render
from ..forms import *
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import redirect
from django.db import connection
from django.utils.datastructures import MultiValueDictKeyError


def administrador(request):
    enlace = link.objects.all()
    enlace2 = linkSecond.objects.all()
    iconos = stockIcon.objects.all()
    lastValue = link.objects.last()
    form2 = PostSubmenu()
    form = PostForm()
    if request.method == "POST":
        form2 = PostSubmenu(request.POST)
        form = PostForm(request.POST)
        
        if form.is_valid() :
            post = form.save(commit=False)
            post.save()
            ser_instance = serializers.serialize('json', [ post, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)        
        
        if form2.is_valid():
            post2 = form2.save(commit=False)
            post2.save()
            
            ser_instance = serializers.serialize('json', [ post2, ])
            
            return JsonResponse({"instance": ser_instance}, status=200)

    else:
        form = PostForm()
        form2 = PostSubmenu()
    #
    contexto = {'link':enlace, 'link2':enlace2, 'icon':iconos,'form': form, 'form2':form2, 'lastValue':lastValue}
    return render(request, 'admin.html', contexto)

    
def delete(request, pk):
    
    record = link.objects.filter(linkP1 = pk)
    record2 = linkSecond.objects.filter(linkP = pk)
    record2.delete()
    record.delete()
    return redirect('admin')

    print("Record doesn't exists")
    #return redirect('actualizar')
        
def delete2(request, pk):
    try:
        record = linkSecond.objects.get(id = pk)
        record.delete()
        return redirect('admin')
    except:
        print("Record doesn't exists")


def update(request, id):
    nombre = request.POST['name']
    descripcion = request.POST['description']
    icono = request.POST['icon']
    # estado = bool(request.POST['state'])
    #enlace = request.POST['enlaceP']

    try:
        estado = bool(request.POST['state'])
    except MultiValueDictKeyError:
        estado= False


    #nombre = 'admin'
    with connection.cursor() as cursor: 
        cursor.execute("UPDATE blog_link SET name = '{name}', description= '{descripcion}', icon = '{icono}', state = {estado} WHERE id = {id}".format(id=id, name=nombre, descripcion=descripcion, icono=icono, estado = estado))
        valor = cursor.fetchone()
        
    contexto = {'valor':valor}
    return render(request,'edit.html' , contexto)


def update2(request, id):
    nombre = request.POST['name']
    descripcion = request.POST['description']
    #icono = request.POST['icon']
    # estado = bool(request.POST['state'])
    enlace = request.POST['enlaceP']
    try:
        estado = bool(request.POST['state'])
    except MultiValueDictKeyError:
        estado= False
    #nombre = 'admin'
    with connection.cursor() as cursor: 
        cursor.execute("UPDATE blog_linkSecond SET name = '{name}', description= '{descripcion}', state = {estado}, enlaceP = '{enlace}' WHERE id = {id}".format(id=id, name=nombre, descripcion=descripcion, estado = estado, enlace = enlace))
        valor = cursor.fetchone()
    contexto = {'valor':valor}
    return render(request,'edit.html' , contexto)


def actualizar(request):
    return render(request, "edit.html")
