  <H1 align="center"> EXTRANET COFARVE </H1>


   <p align="center">
   <img src="https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green/">
   </p>

![License](https://img.shields.io/github/license/Alexm-99/Extranet_Cofarve)

<H2 align="left"> Autor </H2>


[<img src="https://avatars.githubusercontent.com/u/56804056?v=4" style="border-radius:50%" width=115 ><br><sub> Alex Medranda</sub>](https://github.com/Alexm-99)
 

[![medrandacode](https://img.shields.io/youtube/channel/subscribers/UCispOdkxxOE3S_0EfneQK0g?style=social)](https://www.youtube.com/channel/UCispOdkxxOE3S_0EfneQK0g) 



  **Tabla de Contenido**
- [PASOS DE INSTALACIÓN](#pasos-de-instalación)
  - [Requerimientos](#requerimientos)
  - [Migración de modelos](#migración-de-modelos)
      - [comandos](#comandos)
  - [Actualización de datos en base de datos](#actualización-de-datos-en-base-de-datos)
      - [comando](#comando)
  - [Creación de usuario](#creación-de-usuario)
- [INTERFACES DE APLICACIÓN](#interfaces-de-aplicación)
  - [Extranet Cofarve](#extranet-cofarve)
  - [Inicio de sesión](#inicio-de-sesión)
  - [Enlace](#enlace)
  - [Galería](#galería)
  - [Temas Importantes](#temas-importantes)
  - [Redes Sociales](#redes-sociales)
  - [Nuestras Noticias en Redes](#nuestras-noticias-en-redes)
#  PASOS DE INSTALACIÓN
## Requerimientos
  `./requirements.txt`
- Djando 4
- mysqlclient

>(Opcional) Puedes crear un [*entorno virtual*](https://docs.python.org/es/3/tutorial/venv.html) y una vez activado ejecutar los comandos.

Puedes ejecutar el siguiente comando para instalar todos los modulos necesarios para el proyecto.

    pip install -r requirements.txt
##  Migración de modelos

*Ruta del modelo: `./blog/models.py`*
#### comandos	
    python manage.py makemigrations
---
    python manage.py migrate

Estos comandos se aplican para exportar los modelos creados  a la base de datos y poder ejecutar de manera adecuada el sistema.
## Actualización de datos en base de datos
*Ruta de los datos: `./blog/fixtures/`*

> Datos creados en archivos JSON "temas-noticias-icons"
#### comando	
    python manage.py loaddata temas icons noticias

Los datos en los archivos *json* son exportados a la base de datos con el fin de inicializar datos en el proyecto.
## Creación de usuario

    python manage.py createsuperuser
Al ejecutar este comando tendrás que llenar las credenciales de tu nuevo usuario, podrás crear los usuarios que requieras. 

> Username (leave blank to use 'user'): *Un nombre para el Usuario*
> 
> Email address: *Un email para el usuario*
> 
> Password:  *Una contraseña para el usuario*

# INTERFACES DE APLICACIÓN
## Extranet Cofarve
>HTML: `./public/templates/index.html`
>
>CSS:`./public/static/css/Style.css` | `./public/static/css/StyleII.css`
>
>JS: `./public/static/js/index.js`  

![extranet](/imagenDoc/Extranet1.png "Extranet Cofarve")

![extranet](/imagenDoc/Extranet2.png "Extranet Cofarve")
## Inicio de sesión 
>HTML: `./public/templates/registration/login.html`
>
>CSS:`./public/static/css/registration/login.css`
>
>JS: `Sin archivo js` 


Se inicia sesión con las credenciales especificadas en [Creación de usuario](#creación-de-usuario)


![login](/imagenDoc/login.png)
## Enlace

>HTML: `./public/templates/admin.html`
>
>CSS:`./public/static/css/StyleAdmin.css`
>
>JS: `./public/static/js/admin1.js`  
>     `./public/static/js/admin.js` 

Apartado de Enlace, se aplica la configuración de los menús y submenús, aplicaremos los diferentes tipos de enlaces, cada menú contiene diferentes submenus.

![Enlace](/imagenDoc/enlaceDetalle.png "Extranet Cofarve")


## Galería

##  Temas Importantes

## Redes Sociales

## Nuestras Noticias en Redes
