
from ..models import *
from django.shortcuts import render
from ..forms import PostGaleria
from django.http import JsonResponse,HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.db import connection
from django.utils.datastructures import MultiValueDictKeyError
import os
def galeriaConfi(request): 
  
    if request.method == 'POST': 
        form = PostGaleria(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return render(request,'edit.html' )

    else: 
        form = PostGaleria() 
    return render(request, 'galeria.html', {'form' : form}) 
  
def updateimage(request, id):  #this function is called when update data
    old_image = Galeria.objects.get(id=id)
    form = PostGaleria(request.POST, request.FILES, instance=old_image)
    # descripcion = request.POST['description']
    ruta = request.POST['imageX']
    with connection.cursor() as cursor: 
         cursor.execute("UPDATE blog_Galeria SET imageX =  '{ruta}'  WHERE id = {id}".format(id=id, ruta=ruta))
         valor = cursor.fetchone()
           # deleting old uploaded image.
    image_path = old_image.image_document.path
    if os.path.exists(image_path):
        os.remove(image_path)

        return redirect("actualizar")
    else:
        context = {'singleimagedata': old_image, 'form': form}
        return render(request, 'edit.html', context)