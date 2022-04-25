from django.db import models

# Create your models here.


class link(models.Model):
    id = models.CharField (max_length=100 , primary_key=True)
    linkP1 = models.CharField(max_length=100) # codigo de menu
    name = models.CharField(max_length=100)
    enlaceP = models.CharField(max_length=500)
    description = models.CharField(max_length=200)
    icon = models.CharField(max_length=300)
    state = models.BooleanField()

    def __str__(self):
        return self.id

class linkSecond(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    enlaceP = models.CharField(max_length=500)
    description = models.CharField(max_length=200)
    icon = models.CharField(max_length=300)
    state = models.BooleanField()
    linkP = models.CharField(max_length=100) # codigo de menu


    
class Galeria(models.Model):
    id = models.AutoField(primary_key=True)
    imageX = models.FileField(upload_to='public/static/', max_length=254, blank=True)
   

    def __str__(self):
        return self.id


class RedeSociales(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    state = models.BooleanField()
    enlace = models.CharField(max_length=300)


    def __str__(self):
        return self.id


class TemasImportantes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    enlace = models.CharField(max_length=300)


    def __str__(self):
        return self.id

class Noticias(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    enlace = models.CharField(max_length=300)


    def __str__(self):
        return self.id

class administrador(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=100)
    email = models.EmailField()
    passwd = models.CharField(max_length=300)


    def __str__(self):
        return self.id

