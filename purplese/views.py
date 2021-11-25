from django.shortcuts import *
from django.contrib.auth.models import User
from django.views.generic.base import View
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import UpdateView
from django.urls.base import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *

class MeuUpdateView(UpdateView):
    def get(self, request, pk, *args, **kwargs):
        if request.user.id == pk:
            return super().get(request, pk, args, kwargs)
        else:
            return redirect('purplese/registros/homeSec.html')
def paginaSecreta(request):
    return render(request,"purplese/registros/paginaProfile.html")

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

class CreateImagemUsuario(View):
    #Definindo criacao do formulario
    def get(self,request,*args,**kwargs):
        form={'formulario':UsuarioForm}
        return render(request,'purplese/registros/cadastrarImagens.html',form)
    def post(self,request,*args,**kwargs):
        form=UsuarioForm(request.POST)

        if form.is_valid():
            info=form.save()
            info.user=request.user
            info.save()
            return HttpResponseRedirect(reverse_lazy("\purplese\registros\minhasImagens.html"))
        mensagem='Não foi possível cadastrar'
        return render(request,'purplese/registros/cadastrarImagens.html',mensagem)
class ListImagemUsuario(View):
    #Listando imagens cadastradas pelo usuário
    def get(self,request,*args,**kwargs):
        usuario=MeUsuario.objects.filter(user=request.user)
        lista={'usuario':usuario}
        return render(request,'purplese/registros/minhasImagens.html',lista)

class ListaRecentes(View):
    def get(self,request,*args,**kwargs):
        #Ordena em Ordem descrescente e escolhe os 5 primeiros depois de ordendo
        usuario=MeUsuario.objects.all().order_by('-created')[:5]
        lista={'usuario':usuario}
        return render(request,'purplese/registros/recentes.html',lista)
