from ckeditor.widgets import CKEditorWidget
from django import forms

from . import admin
from .models import Post


class PostForm(forms.ModelForm):
    conteudo = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Post
        fields = ('titulo', 'resumo', 'conteudo')



