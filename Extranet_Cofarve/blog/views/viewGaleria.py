
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
  
def updateimage(request, id):  #this function is called when update data
    form = Galeria.objects.get(id=id)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(form.imageX) > 0:
                os.remove(form.imageX.path)
            form.imageX = request.FILES['imageX']
        #form.name = request.POST.get('name')
        form.descripcion = request.POST.get('descripcion')
        #form.price = request.POST.get('price')
        form.save()
        #messages.success(request, "product Updated Successfully")
        return redirect("actualizar")
    context = {'form':form}
    return render(request, 'galeriaUpdate.html', context)



