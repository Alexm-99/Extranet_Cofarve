from ..models import *
from django.shortcuts import render
from ..forms import PostForm, PostSubmenu,PostGaleria
def inicio(request):
    enlace = link.objects.all()
    enlace2 = linkSecond.objects.all()
    temasimportantes = TemasImportantes.objects.all()
    try:

        imagen1 = Galeria.objects.get(id = "1")
        imagen2 = Galeria.objects.get(id = "2")
        imagen3 = Galeria.objects.get(id = "3")
        contexto = {'link':enlace , 'link2':enlace2, 'tema':temasimportantes ,
                     'imagen':imagen1,'imagenx2':imagen2, 'imagenx3':imagen3     }
        return render(request, 'index.html', contexto)
    except:
        
        contexto = {'link':enlace , 'link2':enlace2, 'tema':temasimportantes}
        return render(request, 'index.html', contexto)

