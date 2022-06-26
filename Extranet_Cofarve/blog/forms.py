from django import forms

from .models import TemasImportantes, link,linkSecond,Galeria

class PostForm(forms.ModelForm):

    class Meta:
        model = link
        fields = ('id', 'linkP1', 'name','description','icon', 'state', )
        #id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        
class PostSubmenu(forms.ModelForm):

    class Meta:
        model = linkSecond
        fields = ('id', 'name', 'enlaceP','description','state', 'linkP', )
class PostGaleria(forms.ModelForm):

    class Meta:
        model = Galeria
        fields = ('id', 'imageX', 'descripcion','state' )

class PostTemas(forms.ModelForm):

    class Meta:
        model = TemasImportantes
        fields = ('id', 'name', 'description'  )

