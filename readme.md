  

#  PASOS DE INSTALACIÓN

##  Migración de modelos

*Ruta del modelo: `./blog/models.py`*
#### comandos	
    python manage.py makemigrations
    python manage.py migrate

Estos comandos se aplican para exportar los modelos creados  a la base de datos y poder ejecutar de manera adecuada el sistema.
## Actualización de datos en base de datos
*Ruta de los datos: `./blog/fixtures/`*

> Datos creados en archivos JSON "temas-noticias-icons"

    python manage.py loaddata temas
    python manage.py loaddata noticias
    python manage.py loaddata icons

Los datos en los archivos *json* son exportados a la base de datos con el fin de inicializar datos en el proyecto.
## Creación de usuario 

    python manage.py createsuperuser
Al ejecutar este comando tendrás que llenar las credenciales de tu nuevo usuario, podrás crear los usuarios que requieras. 

> Username (leave blank to use 'user'): *Un nombre para el Usuario*
> 
> Email address: *Un email para el usuario*
> 
> Password:  *Una contraseña para el usuario*

# Interfaces de la aplicación 

## Inicio de sesión 
![login](/imagenDoc/login.png)
## Enlace

## Galería

##  Temas Importantes

## Redes Sociales

## Nuestras Noticias en Redes
