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
  edit = forms.IntegerField(widget = HiddenInput())

  def clean(self):
    cleaned_data = self.cleaned_data
    try:
      ramal = cleaned_data['ramal']
      email = cleaned_data['email']
    except:
      ramal = None
      email = None
    
    #if cleaned_data.has_key( 'edit' ):
    edit = cleaned_data['edit']
    #else:
    #  edit = 0

    up = UserProfile.objects.filter(ramal=ramal)

    if ramal and up:
      if up[0].profile.id != edit:
        self._errors["ramal"] = self.error_class([u"Ramal já cadastrado."])
        raise forms.ValidationError("not unique")

    ue = User.objects.filter(email=email)
    if email and ue:

      if ue[0].id != edit:
        self._errors["email"] = self.error_class([u"Email já cadastrado."])
        raise forms.ValidationError("not unique")
    
    print cleaned_data
    # Always return the full collection of cleaned data.
    return cleaned_data