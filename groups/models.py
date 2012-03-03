# -*- coding:utf-8 -*-
from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=30,blank=False,unique=True,verbose_name='Nome')

    # Permissões básicas:
    can_call_ramal = models.BooleanField(default=True,verbose_name='Permitir chamadas para ramal')
    can_call_emergency = models.BooleanField(default=True,verbose_name='Permitir chamadas de emergência')
    can_call_fix = models.BooleanField(blank=False,default=False,verbose_name='Permitir chamadas para fixo')
    can_call_mobile = models.BooleanField(blank=False,default=False,verbose_name='Permitir chamadas para celular')
    can_call_ddd = models.BooleanField(blank=False,default=False,verbose_name='Permitir chamadas DDD')
    can_call_ddi = models.BooleanField(blank=False,default=False,verbose_name='Permitir chamadas DDI')
    can_call_0800 = models.BooleanField(blank=False,default=False,verbose_name='Permitir chamadas 0800')
    can_call_0300 = models.BooleanField(blank=False,default=False,verbose_name='Permitir chamadas 0300')

    def __unicode__(self):
        return self.name

    #TO-DO:Permissões avançadas
    # many-to-one permission class
