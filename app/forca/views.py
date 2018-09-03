
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
    fields = ['hits', 'erros', 'pontuacaonegativa','pontuacaopositiva', 'verificador']

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
        if ('a' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('a' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('a' == list_secreta[x]):
                        letrasDescobertas[x] = 'a'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('b' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('b' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('b' == list_secreta[x]):
                        letrasDescobertas[x] = 'b'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('c' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('c' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('c' == list_secreta[x]):
                        letrasDescobertas[x] = 'c'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)            

        if ('d' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('d' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('d' == list_secreta[x]):
                        letrasDescobertas[x] = 'd'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('e' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('e' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('e' == list_secreta[x]):
                        letrasDescobertas[x] = 'e'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('f' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('f' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('f' == list_secreta[x]):
                        letrasDescobertas[x] = 'f'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('g' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('g' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('g' == list_secreta[x]):
                        letrasDescobertas[x] = 'g'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('h' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('h' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('h' == list_secreta[x]):
                        letrasDescobertas[x] = 'h'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('i' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('i' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('i' == list_secreta[x]):
                        letrasDescobertas[x] = 'i'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('j' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('j' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('j' == list_secreta[x]):
                        letrasDescobertas[x] = 'j'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('k' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('k' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('k' == list_secreta[x]):
                        letrasDescobertas[x] = 'k'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa) 
        if ('l' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('l' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('l' == list_secreta[x]):
                        letrasDescobertas[x] = 'l'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('m' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('m' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('m' == list_secreta[x]):
                        letrasDescobertas[x] = 'm'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('n' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('n' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('n' == list_secreta[x]):
                        letrasDescobertas[x] = 'n'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('o' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('o' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('o' == list_secreta[x]):
                        letrasDescobertas[x] = 'o'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('p' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('p' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('p' == list_secreta[x]):
                        letrasDescobertas[x] = 'p'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('q' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('q' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('q' == list_secreta[x]):
                        letrasDescobertas[x] = 'q'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('r' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('r' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('r' == list_secreta[x]):
                        letrasDescobertas[x] = 'r'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('s' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            if ('s' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                acerto = partidaatual.hits
                for x in range(len(list_secreta)):
                    if('s' == list_secreta[x]):
                        letrasDescobertas[x] = 's'
                        acerto = acerto + 1 
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)  
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('t' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('t' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('t' == list_secreta[x]):
                        letrasDescobertas[x] = 't'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('u' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('u' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('u' == list_secreta[x]):
                        letrasDescobertas[x] = 'u'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('v' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('v' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('v' == list_secreta[x]):
                        letrasDescobertas[x] = 'v'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('x' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('x' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('x' == list_secreta[x]):
                        letrasDescobertas[x] = 'x'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('w' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('w' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('w' == list_secreta[x]):
                        letrasDescobertas[x] = 'w'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('y' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('y' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('y' == list_secreta[x]):
                        letrasDescobertas[x] = 'y'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)
        if ('z' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            list_secreta = list(partidaatual.word)
            acerto = int(partidaatual.hits)
            if ('z' in list_secreta):
                letrasDescobertas = partidaatual.letters.split()
                for x in range(len(list_secreta)):
                    if('z' == list_secreta[x]):
                        letrasDescobertas[x] = 'z'
                        acerto = acerto + 1
                        models.Partida.objects.filter(usuario=self.request.user.id).update(hits=acerto)
                letrasDescobertas = str(letrasDescobertas)
                models.Partida.objects.filter(usuario=self.request.user.id).update(letters=letrasDescobertas)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                partidaatual.hits = int(partidaatual.hits)
                list_secreta = list(partidaatual.word)
                list_secreta = len(list_secreta)
                if (partidaatual.hits == list_secreta):
                    models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaopositiva=10)
                    models.Partida.objects.filter(usuario=self.request.user.id).update(verificador=1)    
            else:
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                pontuacaonegativa = int(partidaatual.pontuacaonegativa)
                pontuacaonegativa = pontuacaonegativa - 1
                erros = int(partidaatual.erros)
                erros = erros + 1
                models.Partida.objects.filter(usuario=self.request.user.id).update(erros=erros)
                models.Partida.objects.filter(usuario=self.request.user.id).update(pontuacaonegativa=pontuacaonegativa)

    def post(self, request, *args, **kwargs):
        list_secreta = []
        if ('novamente' in self.request.POST):
            partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
            erros = int(partidaatual.erros)
            models.Partida.objects.filter(usuario=self.request.user.id).delete()
            return HttpResponseRedirect('/criarpartida/')
        if ('venceu' in self.request.POST):
            if (models.Ranking.objects.filter(usuario=self.request.user)):
                ranking = models.Ranking.objects.get(usuario=self.request.user.id)
                pontuacao =  int(ranking.pontuacao)
                pontuacao = pontuacao + 10
                models.Ranking.objects.filter(usuario=self.request.user.id).update(pontuacao=pontuacao)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                erros = int(partidaatual.erros)
                models.Partida.objects.filter(usuario=self.request.user.id).delete()
                return HttpResponseRedirect('/home/')
            else:
                models.Ranking.objects.create(usuario=self.request.user,pontuacao= 10)
                partidaatual = models.Partida.objects.get(usuario=self.request.user.id)
                erros = int(partidaatual.erros)
                models.Partida.objects.filter(usuario=self.request.user.id).delete()
                return HttpResponseRedirect('/home/')
        if ('a' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('d' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('g' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('s' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('b' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('c' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('e' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('f' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('h' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('i' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('j' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('k' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('l' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('m' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('n' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('o' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('p' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('q' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('r' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('t' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('u' in self.request.POST):
            return self.get(request, *args, **kwargs)  
        elif ('v' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('x' in self.request.POST):
            return self.get(request, *args, **kwargs) 
        elif ('w' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('y' in self.request.POST):
            return self.get(request, *args, **kwargs)
        elif ('z' in self.request.POST):
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

class Perdeu(ListView):
    model = models.Partida
    template_name = 'core/perdeu.html'

    def get_context_data(self, **kwargs):
        kwargs['partida'] = models.Partida.objects.all()
        return super(Perdeu, self).get_context_data(**kwargs)

class Venceu(ListView):
    model = models.Partida
    template_name = 'core/venceu.html'

    def get_context_data(self, **kwargs):
        kwargs['partida'] = models.Partida.objects.all()
        return super(Venceu, self).get_context_data(**kwargs)

class Ranking(ListView):
    model = models.Ranking
    template_name = 'core/ranking.html'

    def get_context_data(self, **kwargs):
        kwargs['ranking'] = models.Ranking.objects.all().order_by('-pontuacao')
        return super(Ranking, self).get_context_data(**kwargs)

