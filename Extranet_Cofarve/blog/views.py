from django.shortcuts import render
from django.db import connection
from .models import link, linkSecond

# Create your views here.
def inicio(request):
    enlace = link.objects.all()
    enlace2 = linkSecond.objects.all()
    contexto = {'link':enlace , 'link2':enlace2}
    return render(request, 'index.html', contexto)