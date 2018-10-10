from django import forms
from .models import Post, PeR

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

class PERForm(forms.ModelForm):

    class Meta:
        model = PeR
        fields = ('pergunta', 'nome')