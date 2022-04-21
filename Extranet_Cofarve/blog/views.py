from django.shortcuts import render
from django.db import connection
from .models import link

# Create your views here.
def inicio(request):
    enlace = link.objects.all()
    contexto = {'link':enlace}
    return render(request, 'index.html', contexto)