from ..models import *
from django.shortcuts import render
from ..forms import PostForm, PostSubmenu,PostGaleria
def inicio(request):
    enlace = link.objects.all()
    enlace2 = linkSecond.objects.all()
    redes = RedeSociales.objects.all()
    temasimportantes = TemasImportantes.objects.all()
    picture = Galeria.objects.all()
    facebook = Noticias.objects.get(id = 1)
    youtube = Noticias.objects.get(id = 2)

    contexto = {'link':enlace , 'link2':enlace2, 'tema':temasimportantes , 'picture':picture, 'redes':redes,'facebook':facebook, 'youtube':youtube }
    return render(request, 'index.html', contexto)
   
