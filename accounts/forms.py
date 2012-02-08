# -*- coding: utf-8 -*-
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import *
#from django.forms import *

class UserForm(forms.Form):
  def __init__(self, *args, **kwargs):
    super(UserForm, self).__init__(*args, **kwargs)
    self.fields['can_call_ramal'].widget.attrs['disabled'] = 'disabled'
    self.fields['can_call_emergency'].widget.attrs['disabled'] = 'disabled'

  nome = forms.CharField(max_length=40,label="Nome",required=True)
  email = forms.EmailField(max_length=40,label="Email",required=True)
  password = forms.CharField(widget=PasswordInput(render_value=True),max_length=100,label='Senha')
  ramal = forms.IntegerField(required=True,min_value=0)
  admin = forms.BooleanField(required=False,label="Administrador")
  can_call_ramal = forms.BooleanField(required=False,label="Permitir ligações para ramal",initial=True)
  can_call_emergency = forms.BooleanField(required=False,label="Permitir ligações para emergência",initial=True)
  can_call_fix = forms.BooleanField(required=False,label="Permitir ligações para fixo local")
  can_call_mobile = forms.BooleanField(required=False,label="Permitir ligações para celular local")
  can_call_ddd = forms.BooleanField(required=False,label="Permitir ligações DDD")
  can_call_ddi = forms.BooleanField(required=False,label="Permitir ligações DDI")
  can_call_0800 = forms.BooleanField(required=False,label="Permitir ligações 0800")
  can_call_0300 = forms.BooleanField(required=False,label="Permitir ligações 0300")