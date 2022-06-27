
from ..forms import PostRedes
from ..models import RedeSociales
from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.shortcuts import render


def redes(request): 
    red = RedeSociales.objects.all()
    form = PostRedes() 
    if request.method == 'POST':
        form = PostRedes(request.POST) 
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            ser_instance = serializers.serialize('json', [ post, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)        
        
    else: 
        form = PostRedes() 

    contexto = {"red":red, "form":form}
    return render(request, 'redesSociales.html', contexto) 