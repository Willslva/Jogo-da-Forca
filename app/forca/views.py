
# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from . import models

class Index(TemplateView):
    template_name = 'base.html'

class Home(TemplateView):
    template_name = 'home.html'

class Partida(TemplateView):
    template_name = 'jogo.html'

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
