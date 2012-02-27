# -*- coding:utf-8 -*-
from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=30,blank=False,unique=True)

    # Permissões básicas:
    can_call_ramal = models.BooleanField(default=True)
    can_call_emergency = models.BooleanField(default=True)
    can_call_fix = models.BooleanField(blank=False,default=False)
    can_call_mobile = models.BooleanField(blank=False,default=False)
    can_call_ddd = models.BooleanField(blank=False,default=False)
    can_call_ddi = models.BooleanField(blank=False,default=False)
    can_call_0800 = models.BooleanField(blank=False,default=False)
    can_call_0300 = models.BooleanField(blank=False,default=False)

    #TO-DO:Permissões avançadas
    # many-to-one permission class
