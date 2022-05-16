#from readline import parse_and_bind
from multiprocessing import context
from django.shortcuts import render
from django.db import connection
from .models import TemasImportantes, link, linkSecond, Galeria, stockIcon
from .forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils import timezone
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


def administrador(request):
    enlace = link.objects.all()
    enlace2 = linkSecond.objects.all()
    iconos = stockIcon.objects.all()
  
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/administrador/send', pk=post.pk)
    else:
        form = PostForm()


    contexto = {'link':enlace, 'link2':enlace2, 'icon':iconos,'form': form }
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

def update(request, pk):  
    enlace = get_object_or_404(link, pk=pk)  
    if request.method == "POST":
        form = PostForm(request.POST, instance = enlace)  
        if form.is_valid():
            enlace = form.save(commit=False)
            enlace.author = request.user
            enlace.save()
            
            return redirect('actualizar')
    else:
        form = PostForm(instance=enlace)
        return redirect('actualizar')
    contexto = {'form': form }
    return render(request, 'admin.html', contexto)


  


    
    
    
    
    # post = get_object_or_404(request.POST, pk=id)
    # if request.method == "POST":
    #     form = PostForm(request.POST, instance=post)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.name = request.name
    #         post.enlaceP=request.enlaceP
    #         post.published_date = timezone.now()
    #         post.save()
    #         return redirect('post_detail', pk=post.pk)
    # else:
    #     form = PostForm(instance=post)
    # return render(request, 'blog/post_edit.html', {'form': form})