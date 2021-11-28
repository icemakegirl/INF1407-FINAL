from django.shortcuts import *
from django.contrib.auth.models import User
from django.views.generic.base import View
from django.core.paginator import Paginator
from django.http.response import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import UpdateView
from django.urls.base import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from django.http import JsonResponse

class MeuUpdateView(UpdateView):
    def get(self, request, pk, *args, **kwargs):
        if request.user.id == pk:
            return super().get(request, pk, args, kwargs)
        else:
            return redirect('sec-home')
def paginaSecreta(request):
    return render(request,"purplese/registros/home.html")

def homeSec(request):
    return render(request, "purplese/registros/homeSec.html")
# Create your views here.

def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("sec-home")
    else:
        formulario = UserCreationForm()
    context = {'form': formulario}
    return render(request,'purplese/registros/registro.html',context)
def Busca_Tag(request):
    usuario_list=None
    search=None
    if request.method == 'POST':
        formulario = Submete_pesquisa(request.POST)
        if formulario.is_valid():
            search = formulario.cleaned_data["recebe"]
            if search == '':
                usuario_list=MeUsuario.objects.all().order_by('-atualiza_data')[:5]
            else:
                usuario_list = MeUsuario.objects.filter(tag=search.lower())
    else:
        formulario = Submete_pesquisa()
        usuario_list=MeUsuario.objects.all().order_by('-atualiza_data')[:5]
    paginator=Paginator(usuario_list,6)
    page=request.GET.get('page')
    usuario=paginator.get_page(page)
    context={'usuario':usuario,'form':formulario,'bus':search}
    return  render(request,'purplese/registros/Bus_tag.html',context)
def Busca_Genero(request):
    usuario_list=None
    search=None
    if request.method == 'POST':
        formulario = Submete_pesquisa(request.POST)
        if formulario.is_valid():
            search = formulario.cleaned_data["recebe"]
            if search == '':
                usuario_list=MeUsuario.objects.all().order_by('-atualiza_data')[:5]
            else:
                usuario_list = MeUsuario.objects.filter(genero=search.lower())
    else:
        formulario = Submete_pesquisa()
        usuario_list=MeUsuario.objects.all().order_by('-atualiza_data')[:5]
    paginator=Paginator(usuario_list,6)
    page=request.GET.get('page')
    usuario=paginator.get_page(page)
    context={'usuario':usuario,'form':formulario,'bus':search}
    return  render(request,'purplese/registros/Bus_genero.html',context)
def Busca_Categoria(request):
    usuario_list=None
    search=None
    if request.method == 'POST':
        formulario = Submete_pesquisa(request.POST)
        if formulario.is_valid():
            search = formulario.cleaned_data["recebe"]
            if search == '':
                usuario_list=MeUsuario.objects.all().order_by('-atualiza_data')[:5]
            else:
                usuario_list = MeUsuario.objects.filter(categoria=search.lower())
    else:
        formulario = Submete_pesquisa()
        usuario_list=MeUsuario.objects.all().order_by('-atualiza_data')[:5]
    paginator=Paginator(usuario_list,6)
    page=request.GET.get('page')
    usuario=paginator.get_page(page)
    context={'usuario':usuario,'form':formulario,'bus':search}
    return  render(request,'purplese/registros/Bus_categoria.html',context)

def CreateImagemUsuario(request):
    #Definindo criacao do formulario
    if request.user.is_authenticated:
        if request.method == 'POST':
            formulario=UsuarioForm(request.POST or None, request.FILES or None)
            print(formulario.errors)
            
            if formulario.is_valid():
                img=formulario.cleaned_data["imagem"]
                print("foi?",img)
                info=formulario.save(commit=False)
                info.tags=formulario.cleaned_data["tag"].lower()
                info.categoria=formulario.cleaned_data["categoria"].lower()
                info.genero=formulario.cleaned_data["genero"].lower()
                info.user=request.user
                info.save()
                return redirect("list-img")
        else:
            formulario=UsuarioForm()
            print("Invalido")

        usuario={'formulario':formulario}
        return render(request,'purplese/registros/cadastrarImagens.html',usuario) 
    else: 
        return redirect("sec-registro")

class ListImagemUsuario(View):
    #Listando imagens cadastradas pelo usuário
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            usuario=MeUsuario.objects.filter(user=request.user)
            lista={'usuario':usuario}
            return render(request,'purplese/registros/minhasImagens.html',lista)
        return redirect('sec-login')

class ListaRecentes(View):
    def get(self,request,*args,**kwargs):
        #Ordena em Ordem descrescente e escolhe os 5 primeiros depois de ordendo
        usuario_list=MeUsuario.objects.all().order_by('-atualiza_data')[:5]
        paginator=Paginator(usuario_list,6)
        page=request.GET.get('page')
        usuario=paginator.get_page(page)
        lista={'usuario':usuario}
        return render(request,'purplese/registros/recentes.html',lista)
class ImageDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        usuario = MeUsuario.objects.filter(pk=pk)
        context = {'pessoa': usuario, }
        return render(request, 'purplese/registros/ApagaImagem.html',context)
    def post(self, request, pk, *args, **kwargs):
        usuario= MeUsuario.objects.filter(pk=pk)
        usuario.delete()
        print("Removendo o contato", pk)
        return redirect("list-img")  
class AtualizaImagem(View):
    def get(self, request, pk, *args, **kwargs):
        usuario= MeUsuario.objects.get(pk=pk)
        formulario = UsuarioForm(instance=usuario)
        context = {'pessoa': formulario, }
        return render(request, 'purplese/registros/atualizaImagem.html', context)

    def post(self, request, pk, *args, **kwargs):
        usuario= MeUsuario.objects.get(pk=pk)
        formulario = UsuarioForm(request.POST, request.FILES,instance=usuario)
        if formulario.is_valid():
            usuario = formulario.save()
            usuario.save()
            return  redirect("list-img")
        else:
            context = {'pessoa': formulario, }
            return render(request, 'contatos/atualizaContato.html', context)
def verificaUsername(request):
    username = request.GET.get("username", None)
    print(username)
    resposta = {
        'existe':
        User.objects.filter(username__iexact=username)
        .exists()}
    return JsonResponse(resposta)
def verificaEmail(request):
    email = request.GET.get("email", None)
    print(email)
    resposta = {
        'existe':
        User.objects.filter(email__iexact=email)
        .exists()}
    print(resposta)
    return JsonResponse(resposta)
def verificaPassword(request):
    senha = request.GET.get("senha", None)
    print(senha)
    resposta = {'existe':senha}
    return JsonResponse(resposta)


