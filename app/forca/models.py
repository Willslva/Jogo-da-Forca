# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import uuid


from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid
from django.db import models


# CreateUpdateModel
# - - - - - - - - - - - - - - - - - - -
class CreateUpdateModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        abstract = True


# UUIDUser
# - - - - - - - - - - - - - - - - - - -
class UUIDUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(Group, blank=True, related_name="uuiduser_set", related_query_name="user")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="uuiduser_set", related_query_name="user")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

class Palavra(models.Model):
    user = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='users', verbose_name='Usuário')
    nome = models.CharField(max_length=255, verbose_name='Palavra')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Palavra'
        verbose_name_plural = 'Palavras'


class Partida(models.Model):
    usuario = models.ForeignKey(UUIDUser,on_delete=models.CASCADE,related_name="user",verbose_name='Usuário')
    word = models.CharField(max_length=100, verbose_name = 'Palavra secreta')
    hits = models.IntegerField(verbose_name = 'Acertos')
    erros = models.IntegerField(verbose_name = 'Erros')
    letters = models.CharField(max_length=100,verbose_name = 'Palavras usadas')

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'
