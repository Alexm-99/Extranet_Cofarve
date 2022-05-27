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
from django.views.generic.base import TemplateView # new
from blog.views import inicio, administrador, galeria,actualizar, delete, update, delete2, update2
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # new

    path('',inicio, name= 'index'),
    path('administrador/',login_required(administrador), name= 'admin'),
    path('galeria/',login_required(galeria), name= 'galeria'), 

    path('administrador/send/',login_required(actualizar), name= 'actualizar'),
    path('delete/<int:pk>', login_required(delete), name="delete"),
    path('administrador/update/<int:id>', login_required(update), name="update"), 
    path('administrador/update2/<int:id>', login_required(update2), name="update2"),
    path('deleteSubmenu/<int:pk>',login_required(delete2), name='delete2',)

]

