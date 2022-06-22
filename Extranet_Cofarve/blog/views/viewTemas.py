from ..forms import PostTemas
from ..models import TemasImportantes
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers


def temasImportantes(request): 
    temas = TemasImportantes.objects.all()
    form = PostTemas()
    if request.method == 'POST': 
        if form.is_valid() :
            post = form.save(commit=False)
            post.save()
            ser_instance = serializers.serialize('json', [ post, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200) 

    else: 
        form = PostTemas() 

    contexto = {"temas":temas, "form":form}
    return render(request, 'temas.html', contexto) 