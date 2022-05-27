#from readline import parse_and_bind
from multiprocessing import context
from traceback import format_stack
from urllib.request import Request
from django.shortcuts import render
from django.db import connection
from .models import TemasImportantes, link, linkSecond, Galeria, stockIcon
from .forms import PostForm, PostSubmenu
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils import timezone

from django.views.generic.edit import FormView
from django.http import JsonResponse,HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

import json
# pon el import de la librerías mas arriba junto a tus otros imports
# ...



# Create your views here.



def inicio(request):
    enlace = link.objects.all()
    enlace2 = linkSecond.objects.all()
    temasimportantes = TemasImportantes.objects.all()
    imagen1 = Galeria.objects.get(id = "1")
    imagen2 = Galeria.objects.get(id = "2")
    imagen3 = Galeria.objects.get(id = "3")
    contexto = {'link':enlace , 'link2':enlace2, 'tema':temasimportantes ,
                 'imagen':imagen1,'imagenx2':imagen2, 'imagenx3':imagen3     }
    return render(request, 'index.html', contexto)

def postLink(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/administrador/send', pk=post.pk)
    else:
        form = PostForm()
        return form

# def postLink2(request):
#     form2 = PostSubmenu()
#     if request.method == "POST":
#         form2 = PostSubmenu(request.POST)
#         if form2.is_valid():
#             post = form2.save(commit=False)
#             post.save()
#             return redirect('/administrador/send', pk=post.pk)
#     else:
#         form2 = PostSubmenu()
#         return form2


def administrador(request):
    enlace = link.objects.all()
    enlace2 = linkSecond.objects.all()
    iconos = stockIcon.objects.all()

    form2 = PostSubmenu()
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        form2 = PostSubmenu(request.POST)
        if form.is_valid() :
            post = form.save(commit=False)
            post.save()
            return redirect('/administrador/send', pk=post.pk)
            #data = json.dumps({'status': 'OK'})
            #return HttpResponse(data, content_type="application/json", status=200)
            #return JsonResponse({"name": name}, status=200)
        
        
        if form2.is_valid():
            post2 = form2.save(commit=False)
            post2.save()
            return redirect('/administrador/send', pk=post2.pk)

    else:
        form = PostForm()
        form2 = PostSubmenu()


  
        
    try:
        variable = request.POST['buscando']
        print(variable)
        with connection.cursor() as cursor: 
            cursor.execute("SELECT file FROM blog_link WHERE id = '"+ variable +"'")
            filtroId = cursor.fetchone()
    except:
        filtroId= ['public/static/articulospdf/intro.pdf']
        print(filtroId)

    
    #form2 = postLink2(request)
    contexto = {'link':enlace, 'link2':enlace2, 'icon':iconos,'form': form, 'form2':form2, 'filtroId':filtroId }
    return render(request, 'admin.html', contexto)



def galeria(request):
    return render(request, "galeria.html")

def actualizar(request):
    return render(request, "edit.html")


def delete(request, pk):
    try:
        record = link.objects.get(id = pk)
        record.delete()
        return redirect('actualizar')
    except:
        print("Record doesn't exists")

def delete2(request, pk):
    try:
        record = linkSecond.objects.get(id = pk)
        record.delete()
        return redirect('actualizar')
    except:
        print("Record doesn't exists")


#@login_required
def update(request, id):
    nombre = request.POST['name']
    descripcion = request.POST['description']
    icono = request.POST['icon']
    # estado = bool(request.POST['state'])
    enlace = request.POST['enlaceP']

    try:
        estado = bool(request.POST['state'])
    except MultiValueDictKeyError:
        estado= False


    #nombre = 'admin'
    with connection.cursor() as cursor: 
        cursor.execute("UPDATE blog_link SET name = '{name}', description= '{descripcion}', icon = '{icono}', state = {estado}, enlaceP = '{enlace}' WHERE id = {id}".format(id=id, name=nombre, descripcion=descripcion, icono=icono, estado = estado, enlace = enlace))
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

   