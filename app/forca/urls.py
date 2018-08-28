# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views as core

app_name = 'forca'

urlpatterns = [
    # Index
     path('', core.Index.as_view(template_name='core/base.html'), name='index'),
    # Login
     path('login/', auth_views.LoginView.as_view(template_name='user/auth.html'), name='login'),

    # Logout
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #home
     path('home/', core.Home.as_view(template_name='core/home.html'), name='home'),

    #Cadastro de usuario
     path('usuarios/novo/', core.UserCreateView.as_view(), name='user-create'),

    #Cadastro de palavra
     path('palavra/nova/', core.WordCreateView.as_view(), name='word-create'),

    #Criar partida
     path('criarpartida/', core.PartidaCreate.as_view(), name='criarpartida'),

    #Game
     path('jogo/', core.Game.as_view(), name='game'),

]
