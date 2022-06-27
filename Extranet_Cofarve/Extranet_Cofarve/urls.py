"""Extranet_Cofarve URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin,auth
from django.urls import path,include
from django.views.generic.base import TemplateView

from blog.views import viewIndex, viewsEnlace,viewGaleria, viewRedes, viewTemas, viewNoticias

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),

    #INICIO DE SESIÓN
    path("accounts/", include("django.contrib.auth.urls")),  # new

    # INDEX
    path('', viewIndex.inicio, name= 'index'),

    # ADMINISTRADOR ENLACE
    path('administrador/',login_required(viewsEnlace.administrador), name= 'admin'),
    path('administrador/send/',login_required(viewsEnlace.actualizar), name= 'actualizar'),
    path('delete/<str:pk>', login_required(viewsEnlace.delete), name="delete"),
    path('administrador/update/<int:id>', login_required(viewsEnlace.update), name="update"), 
    path('administrador/update2/<int:id>', login_required(viewsEnlace.update2), name="update2"),
    path('deleteSubmenu/<int:pk>',login_required(viewsEnlace.delete2), name='delete2'),

    #GALERIA
    path('galeria/',login_required(viewGaleria.galeriaConfi), name= 'galeria'),
    path('galeria/update/State/<int:id>', login_required(viewGaleria.updateState), name="updateState"), 
    path('galeria/update/StateF/<int:id>', login_required(viewGaleria.updateStateF), name="updateStateF"),
    path('deleteimagen/<int:pk>', login_required(viewGaleria.deleteGaleria), name="deleteimagen"),

    # REDES SOCIALES
    path('redes-sociales/',login_required(viewRedes.redes), name= 'RedesSociales'), 
    path('redes/update-redes/<int:id>', login_required(viewRedes.updateR), name="updateRedes"), 
    path('redes/delete/<str:pk>', login_required(viewRedes.deleteRedes), name="deleteRedes"), 

    # TEMAS IMPORTANTES 
    path('temas-importantes/',login_required(viewTemas.temasImportantes), name= 'temas'), 
    path('Temas/updateTemas/<int:id>', login_required(viewTemas.updateT), name="updateTemas"), 

    # NOTICIAS O NUESTRAS REDES 
    path('noticias/',login_required(viewNoticias.noticia), name= 'noticias'), 
   path('oticias/update/<int:id>', login_required(viewNoticias.updateNoticias), name="updateNoticias"), 
  
   

 
    



]
if settings.DEBUG: 
     urlpatterns += static(settings.MEDIA_URL, 
                               document_root=settings.MEDIA_ROOT) 

