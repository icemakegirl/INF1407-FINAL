from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

class MeUsuario(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=CASCADE)
    nome=models.CharField(null=False,max_length=40, help_text='Entre com o Nome da sua imagem')
    imagem = models.ImageField(upload_to='static/img_upload/',max_length=500,null=False,blank=False)
    categoria = models.CharField(null=False,max_length=40, help_text='Entre com a Categoria da sua imagem')
    genero = models.CharField(null=False,max_length=40, help_text='Entre com a Genero da sua imagem')
    tag = models.CharField(null=False,max_length=40, help_text='Entre com a Tag da sua imagem')
    descricao = models.TextField()
    criaca_data=models.DateTimeField(null=False,auto_now_add=True)
    atualiza_data=models.DateTimeField(null=False,auto_now=True)

    def __str__(self):
        return self.nome
    


# Create your models here.
