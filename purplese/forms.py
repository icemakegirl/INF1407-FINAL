from django import forms
from .models import MeUsuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=MeUsuario
        fields = ('nome', 'imagem','categoria','genero','tag','descricao')