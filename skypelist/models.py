# -*- coding:utf8 -*-

from django.db import models

class skypeuser(models.Model):
	ramal = models.PositiveIntegerField(unique=True,blank=False)
	username = models.CharField(max_length=50,blank=False,verbose_name='Usuário Skype',unique=True)
