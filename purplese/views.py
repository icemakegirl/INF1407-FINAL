from django.shortcuts import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class MeuUpdateView(UpdateView):
 def get(self, request, pk, *args, **kwargs):
    if request.user.id == pk:
        return super().get(request, pk, args, kwargs)
    else:
        return redirect('sec-home')
def paginaSecreta(request):
    return render(request,'registros/paginaProfile.html')

def homeSec(request):
 return render(request, "registros/homeSec.html")
# Create your views here.

def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("registros/homeSec.html")
    else:
        formulario = UserCreationForm()
    context = {'form': formulario}
    return render(request,'registros/registro.html',context)
