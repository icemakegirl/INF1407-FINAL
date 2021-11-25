from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
class Categoria(models.Model):
    categoria = models.CharField(null=False,max_length=40, help_text='Entre com a Categoria da sua imagem')
    def __str__(self):
        return self.categoria

class Tag(models.Model):
    tag = models.CharField(null=False,max_length=40, help_text='Entre com a Tag da sua imagem')
    def __str__(self):
        return self.tag

class Genero(models.Model):
    genero = models.CharField(null=False,max_length=40, help_text='Entre com a Genero da sua imagem')
    def __str__(self):
        return self.genero
class MeUsuario(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=CASCADE)
    nome=models.CharField(null=False,max_length=40, help_text='Entre com o Nome da sua imagem')
    imagem = models.ImageField(upload_to='static/img_upload')
    categoria = models.ManyToManyField(Categoria)
    genero = models.ManyToManyField(Genero)
    tag = models.ManyToManyField(Tag)
    descricao = models.TextField()
    criaca_data=models.DateTimeField(null=False,auto_now_add=True)
    atualiza_data=models.DateTimeField(null=False,auto_now=True)

    def __str__(self):
        return str(self.descricao)
    


# Create your models here.
