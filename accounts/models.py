from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
    profile = models.ForeignKey(User,unique=True)
    ramal = models.PositiveIntegerField(unique=True,blank=False,required=True)
    admin = models.BooleanField(required=True,default=False)
    #can_call_ramal = models.BooleanField(default=True)
    #can_call_emergency = models.BooleanField(default=True)
    can_call_fix = models.BooleanField(required=True,default=False)
    can_call_mobile = models.BooleanField(required=True,default=False)
    can_call_ddd = models.BooleanField(required=True,default=False)
    can_call_ddi = models.BooleanField(required=True,default=False)
    can_call_0800 = models.BooleanField(required=True,default=False)
    can_call_0300 = models.BooleanField(required=True,default=False)