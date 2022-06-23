
from multiprocessing import context
from ..models import *
from django.shortcuts import render
from ..forms import PostGaleria
from django.http import JsonResponse,HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.db import connection
from django.utils.datastructures import MultiValueDictKeyError
import os
from django.views.decorators.csrf import csrf_exempt
import cgi
from django.dispatch import receiver

def galeriaConfi(request): 
    picture = Galeria.objects.all()
    if request.method == 'POST': 
        form = PostGaleria(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return render(request,'edit.html' )

    else: 
        form = PostGaleria() 
    contexto = {'form' : form, 'picture' : picture}
    return render(request, 'galeria.html', contexto) 
  



@csrf_exempt
def updateState(request, id): 
    try:
        estado = bool(request.POST['state'])
        print(estado)
    except MultiValueDictKeyError:
        estado= True
        
    #nombre = 'admin'
    with connection.cursor() as cursor: 
        cursor.execute("UPDATE blog_Galeria SET state = {estado} WHERE id = {id}".format(id=id, estado = estado))
        valor = cursor.fetchone()
        
    # contexto = {'valor':valor}
    return render(request,'edit.html')

    
@csrf_exempt
def updateStateF(request, id): 
    try:
        estado = bool(request.POST['state'])
        print(estado)
    except MultiValueDictKeyError:
        estado= False
        
    #nombre = 'admin'
    with connection.cursor() as cursor: 
        cursor.execute("UPDATE blog_Galeria SET state = {estado} WHERE id = {id}".format(id=id, estado = estado))
        valor = cursor.fetchone()
        
    # contexto = {'valor':valor}
    return render(request,'edit.html')

def deleteGaleria(request, pk):
    # os.remove()
    record = Galeria.objects.filter(id = pk)
    record.delete()

    return redirect('galeria')


@receiver(models.signals.post_delete, sender=Galeria)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.imageX:
        if os.path.isfile(instance.imageX.path):
            os.remove(instance.imageX.path)




