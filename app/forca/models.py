# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import uuid


from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Group, Permission
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

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

class Palavra(models.Model):
    id_user = models.ForeignKey(UUIDUser,on_delete=models.CASCADE,verbose_name='usuário')
    nome = models.CharField(max_length=255, verbose_name='Palavra')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Palavra'
        verbose_name_plural = 'Palavras'


class Partida(models.Model):
    usuario = models.ForeignKey(UUIDUser,on_delete=models.CASCADE,verbose_name='Usuário')
    word = models.ForeignKey(Palavra,on_delete=models.CASCADE,verbose_name='Palavra')
    hits = models.IntegerField()
    erros = models.IntegerField(default=0)
    letters = models.CharField(max_length=100)


    class Meta:
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'
