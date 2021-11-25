"""Trabalho_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from purplese import views
app_name = 'purplese'
from django.contrib.auth.models import *
from django.views.generic.edit import UpdateView
from django.urls.base import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetDoneView, PasswordResetView,PasswordResetConfirmView,PasswordResetCompleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('purplese/', views.homeSec,name="sec-home"),
    path('purplese/profile/',views.paginaSecreta,name='sec-paginaSecreta'),
    path('purplese/registro/',views.registro,name='sec-registro'),
    path('purplese/login/', LoginView.as_view(template_name='purplese/registros/login.html'),name='sec-login'),
    path('purplese/logout/',LogoutView.as_view(next_page=reverse_lazy('sec-home')),name='sec-logout'),
    path('purplese/senhaTrocada/',PasswordChangeView.as_view(template_name='purplese/registros/password_change_done.html'),name='sec-passwordDone'),
    path('purplese/trocaSenha/',PasswordChangeView.as_view(template_name='purplese/registros/password_change_form.html',success_url=reverse_lazy('sec-passwordDone')),name='sec-passwordchange'),
    path('purplese/terminaRegistro/<int:pk>/',views.MeuUpdateView.as_view(template_name='purplese/registros/user_form.html',success_url=reverse_lazy('sec-paginaSecreta',
    model=User,fields=['first_name','last_name','email'])),name='sec-completaDados'),
    path('purplese/password_reset/', PasswordResetView.as_view(
 template_name='registros/password_reset_form.html',success_url=reverse_lazy('sec-password_reset_done'),
 email_template_name='registros/password_reset_email.html',subject_template_name='purplese/registros/password_reset_subject.txt',
 from_email='fale.joanne@gmail.com',), name='password_reset'),
 path('purplese/password_reset_done/', PasswordResetDoneView.as_view(template_name='purplese/registros/password_reset_done.html',
 ), name='sec-password_reset_done'),
 path('purplese/password_reset_confirm/<uidb64>/<token>/',
 PasswordResetConfirmView.as_view(template_name='registros/password_reset_confirm.html',
 success_url=reverse_lazy('sec-password_reset_complete'),), name='password_reset_confirm'),
path('purplese/password_reset_complete/', PasswordResetCompleteView.as_view(
 template_name='purplese/registros/password_reset_complete.html'
 ), name='sec-password_reset_complete'),
path('purplese/CadastraImagem/',views.CreateImagemUsuario.as_view(),name='cad-img'),
path('purplese/ListaImagem/',views.CreateImagemUsuario.as_view(),name='list-img'),
path('purplese/Recentes/',views.ListaRecentes.as_view(),name='list-recentes'),
]
