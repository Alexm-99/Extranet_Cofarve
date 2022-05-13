#from readline import parse_and_bind
from django.shortcuts import render
from django.db import connection
from .models import TemasImportantes, link, linkSecond, Galeria, stockIcon
from .forms import PostForm
from django.shortcuts import redirect
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
            post.author = request.user
            post.published_date = timezone.now()
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

def update(request, id):  
    area = link.objects.get(id=id)  
    form = PostForm(request.POST, instance = area)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'areaUpdate': area})  