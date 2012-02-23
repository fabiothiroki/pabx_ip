# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import User



class UserProfile(models.Model):
    profile = models.ForeignKey(User,unique=True)
    ramal = models.PositiveIntegerField(unique=True,blank=False)
    passw = models.CharField(max_length=30,default='')
    admin = models.BooleanField(blank=False,default=False)
    #group = models.ForeignKey(Group,blank=True,null=True )


