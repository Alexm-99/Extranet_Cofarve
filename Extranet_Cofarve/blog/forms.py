from django import forms

from .models import link

class PostForm(forms.ModelForm):

    class Meta:
        model = link
        fields = ('id', 'linkP1', 'name', 'enlaceP','description','icon', 'state', )
        