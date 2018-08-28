
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



class Index(TemplateView):
    template_name = 'core/base.html'

class Home(TemplateView):
    template_name = 'core/home.html'

class PartidaCreate(CreateView):
    model = models.Partida
    template_name = 'core/criarpartida.html'
    success_url = reverse_lazy('forca:game')
    fields = ['hits', 'erros', 'letters']

    def get_context_data(self, **kwargs):
        kwargs['partida'] = models.Partida.objects.all()
        return super(PartidaCreate, self).get_context_data(**kwargs)
        
    def form_valid(self, form):
        max_id = models.Palavra.objects.all().aggregate(max_id=Max("id"))['max_id']
        pk = random.randint(1, max_id)
        global palavraEscolhida
        palavraEscolhida  = str(models.Palavra.objects.get(pk=pk))
        obj = form.save(commit=False)
        global x
        x = obj.letters
        obj.word = palavraEscolhida
        obj.usuario = self.request.user
        obj.save()
        return super(PartidaCreate, self).form_valid(form)

class Game(ListView):
    model = models.Partida
    template_name = 'core/jogo.html'
    
    def post(self, request, *args, **kwargs):
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
