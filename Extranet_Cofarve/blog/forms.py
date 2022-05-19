from django import forms

from .models import link,linkSecond

class PostForm(forms.ModelForm):

    class Meta:
        model = link
        fields = ('id', 'linkP1', 'name', 'enlaceP','description','icon', 'state', )
        #id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
class PostSubmenu(forms.ModelForm):

    class Meta:
        model = linkSecond
        fields = ('id', 'name', 'enlaceP','description','state', 'linkP', )
