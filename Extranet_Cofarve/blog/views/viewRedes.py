
from ..forms import PostGaleria
from django.shortcuts import render



def redes(request): 
  
    if request.method == 'POST': 
        form = PostGaleria(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return render(request,'edit.html' )

    else: 
        form = PostGaleria() 
    return render(request, 'redesSociales.html', {'form' : form}) 