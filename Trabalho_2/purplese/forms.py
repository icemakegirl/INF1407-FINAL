from django import forms
from .models import MeUsuario

class UsuarioForm(forms.ModelForm):
    #imagem = forms.ImageField()
    class Meta:
        model=MeUsuario
        fields = ('nome', 'imagem','categoria','genero','tag','descricao')
    nome=forms.CharField(max_length=40)
    imagem = forms.ImageField()
    categoria = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)
    tag = forms.CharField(max_length=40)
    descricao = forms.CharField(max_length=200, widget=forms.Textarea)

class Submete_pesquisa(forms.Form):
    recebe=forms.CharField(max_length=200)

    