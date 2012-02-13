# -*- coding:utf8 -*-

from django.db import models

class server(models.Model):
    url = models.CharField(max_length=50,blank=False,verbose_name='Endereço')
    port = models.PositiveIntegerField(max_length=50,blank=False,verbose_name='Porta')
    username = models.CharField(max_length=50,verbose_name='Usuário')
    password = models.CharField(max_length=50,)