from ..forms import PostGaleria
from ..models import Galeria
from django.shortcuts import render



def temasImportantes(request): 
    media = Galeria.objects.all()
    # if request.method == 'POST': 
        
  
    #     if form.is_valid(): 
    #         form.save() 
    #         return render(request,'edit.html' )

    # else: 
    #     form = PostGaleria() 

    contexto = {"media":media}
    return render(request, 'temas.html', contexto) 