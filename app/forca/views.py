
# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from . import models
from django.db.models import Max
import random

class Index(TemplateView):
    template_name = 'core/base.html'

class Home(TemplateView):
    template_name = 'core/home.html'

class PartidaCreate(CreateView):
	model = models.Partida
	template_name = "core/jogo.html"
	fields = ['word','hits', 'erros', 'letters']

	
	def get_queryset(self):
		limiteErros = 6
		hits = 0
		erros = 0
		max_id = models.Palavra.objects.all().aggregate(max_id=Max("id"))['max_id']
		pk = random.randint(1, max_id)
		palavraEscolhida  = models.Palavra.objects.get(pk=pk)
		
		
		
	def get_context_data(self, **kwargs):
		kwargs['partida'] = models.Partida.objects.all()
		return super(PartidaCreate, self).get_context_data(**kwargs)


class UserCreateView(CreateView):
	model = models.UUIDUser
	template_name = 'form.html'
	success_url = reverse_lazy('forca:home')
	fields = ['username','first_name', 'last_name', 'password', 'email']
	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()
		return super(UserCreateView, self).form_valid(form)

class WordCreateView(CreateView):
	model = models.Palavra
	template_name = 'formword.html'
	success_url = reverse_lazy('forca:home')
	fields = ['nome']

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.id_user = self.request.user
		obj.save()
		return super(WordCreateView, self).form_valid(form)
