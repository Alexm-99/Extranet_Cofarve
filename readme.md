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
    - [__Tomar enlace de Facebok__](#tomar-enlace-de-facebok)
    - [__Tomar enlace de YouTube__](#tomar-enlace-de-youtube)
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
>      `./public/static/js/validaciones.js` 

Apartado de Enlace, se aplica la configuración de los menús y submenús, aplicaremos los diferentes tipos de enlaces, cada menú contiene diferentes submenus.

![Enlace](/imagenDoc/enlaceDetalle.png "Extranet Cofarve")


## Galería
>HTML: `./public/templates/Galeria.html`
>
>CSS:`./public/static/css/GaleriaStyle.css`
>
>JS: `./public/static/js/Galeria.js`  
 

Apartado de Galeria, se aplica la configuración de la galeria en el index de la aplicación.
![Enlace](/imagenDoc/Galeria.png "Extranet Cofarve")
***
Este apartado es para añadir una nueva imagen.

![Enlace](/imagenDoc/AddGaleria.png "Extranet Cofarve")
##  Temas Importantes
>HTML: `./public/templates/temas.html`
>
>CSS:`./public/static/css/styleII.css`
>
>JS: `./public/static/js/validaciones.js`  
 

Apartado de Temas, se aplica la configuración de temas de relavancia.

![Enlace](/imagenDoc/Temas.png "Extranet Cofarve")
***
## Redes Sociales
Apartado de Redes Sociales, se aplica la configuración de las redes en la extranet, es parecia a la configuración de enlaces.
Cuenta con 16 iconos de diferentes redes sociales.

![Enlace](/imagenDoc/redes.png "Extranet Cofarve")
***
## Nuestras Noticias en Redes
Apartado de noticias en redes, se aplica la configuración de las noticias en facebook y youtube en la extranet.


![Enlace](/imagenDoc/noticias.png "Extranet Cofarve")



### __Tomar enlace de Facebok__

![Enlace](/imagenDoc/url_facebook.png "Extranet Cofarve")
***
### __Tomar enlace de YouTube__
Selecciona el botón Compartir

![Enlace](/imagenDoc/yt1.png "Extranet Cofarve")

Luego seleccionamos solo la parte final del video

![Enlace](/imagenDoc/yt2.png "Extranet Cofarve")
***

![Enlace](/imagenDoc/noti2.png "Extranet Cofarve")