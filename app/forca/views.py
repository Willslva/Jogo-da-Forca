
# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from . import models
from django.db.models import Max
import random
from .forms import UUIDUserForm
from django.http import HttpResponseRedirect



class Index(TemplateView):
    template_name = 'core/base.html'

class Home(TemplateView):
    template_name = 'core/home.html'

class PartidaCreate(CreateView):
    model = models.Partida
    template_name = 'core/criarpartida.html'
    success_url = reverse_lazy('forca:game')
    fields = ['hits', 'erros']

    def get_context_data(self, **kwargs):
        kwargs['partida'] = models.Partida.objects.all()
        return super(PartidaCreate, self).get_context_data(**kwargs)

    def form_valid(self, form): 
        if (models.Partida.objects.filter(usuario=self.request.user)):
            return HttpResponseRedirect('/jogo/')
        else:            
            max_id = models.Palavra.objects.all().aggregate(max_id=Max("id"))['max_id']
            pk = random.randint(1, max_id)
            global palavraEscolhida
            palavraEscolhida  = str(models.Palavra.objects.get(pk=pk))
            global letrasDescobertas
            letrasDescobertas = []
            secredo = list(palavraEscolhida)
            for i in range(len(secredo)):
                letrasDescobertas.append("-")
            letras = str(letrasDescobertas)
            obj = form.save(commit=False)
            obj.letters = letras
            obj.word = palavraEscolhida
            obj.usuario = self.request.user
            obj.save()
            return super(PartidaCreate, self).form_valid(form)
    

class Game(ListView):
    model = models.Partida
    template_name = 'core/jogo.html'

    def get_queryset(self):
        acerto = 0
        if ('a' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            if ('a' in list_secreta):
                print ('Voce e o cara')
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('a' == list_secreta[x]):
                        letrasDescobertas[x] = 'a'
                        print (letrasDescobertas)
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                
        if ('d' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            if ('d' in list_secreta):
                print ('Voce e o cara')
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('d' == list_secreta[x]):
                        letrasDescobertas[x] = 'd'
                        print (letrasDescobertas)
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
        if ('g' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            if ('g' in list_secreta):
                print ('Voce e o cara')
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('g' == list_secreta[x]):
                        letrasDescobertas[x] = 'g'
                        print (letrasDescobertas)
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
        if ('s' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            if ('s' in list_secreta):
                print ('Voce e o cara')
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('s' == list_secreta[x]):
                        letrasDescobertas[x] = 's'
                        acerto = acerto + 1 
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
    def post(self, request, *args, **kwargs):
        list_secreta = []
        if ('a' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('d' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('g' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('s' in self.request.POST):
            return self.get(request, *args, **kwargs)
       

    def get_context_data(self, **kwargs):
        kwargs['partida'] = models.Partida.objects.all()
        return super(Game, self).get_context_data(**kwargs)

class UserCreateView(CreateView):
    model = models.UUIDUser
    template_name = 'user/form.html'
    success_url = reverse_lazy('forca:login')
    form_class = UUIDUserForm
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(obj.password)
        obj.save()
        return super(UserCreateView, self).form_valid(form)


class WordCreateView(CreateView):
	model = models.Palavra
	template_name = 'core/formword.html'
	success_url = reverse_lazy('forca:home')
	fields = ['nome']
	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()
		return super(WordCreateView, self).form_valid(form)
