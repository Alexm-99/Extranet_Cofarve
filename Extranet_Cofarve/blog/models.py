from unicodedata import name
from django.db import models

# Create your models here.


class link(models.Model):
    id = models.AutoField( primary_key=True)
    linkP1 = models.CharField(max_length=100) # codigo de menu
    name = models.CharField(max_length=100)
    #enlaceP = models.CharField(max_length=500)
    description = models.CharField(max_length=200, blank=True)
    icon = models.CharField(max_length=300)
    state = models.BooleanField()

    def __str__(self):
        return self.id

class linkSecond(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    enlaceP = models.CharField(max_length=500)
    description = models.CharField(max_length=200, blank=True)
    state = models.BooleanField()
    linkP = models.CharField(max_length=100) # codigo de menu
    def __str__(self):
        return self.id

    
class Galeria(models.Model):
    id = models.AutoField(primary_key=True)
    imageX = models.FileField(upload_to='imagenes', max_length=254, blank=True)
    descripcion= models.CharField(max_length=300, blank=True)
    state = models.BooleanField(default=False)

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
    #enlace = models.CharField(max_length=300)


    def __str__(self):
        return self.id

class Noticias(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    enlace = models.CharField(max_length=300)


    def __str__(self):
        return self.id


class stockIcon(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


    def __str__(self):
        return self.id