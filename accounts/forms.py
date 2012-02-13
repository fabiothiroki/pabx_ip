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
  password = forms.CharField(widget=PasswordInput(render_value=True),max_length=100,label='Senha',required=True)
  password2 = forms.CharField(widget=PasswordInput(render_value=True),max_length=100,label='Confirmação de Senha',required=True)
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
    ramal = cleaned_data.get('ramal')
    email = cleaned_data.get('email')
    password = cleaned_data.get("password")
    confirm_password = cleaned_data.get("password2")
    
    #if cleaned_data.has_key( 'edit' ):
    edit = cleaned_data['edit']
    #else:
    #  edit = 0

    if password != confirm_password:
      self._errors["password"] = self.error_class([u"As senhas digitadas são diferentes."])
      self._errors["password2"] = self.error_class([u"As senhas digitadas são diferentes."])

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
    
    # Always return the full collection of cleaned data.
    return cleaned_data

class OnlyUserForm(forms.Form):
  def __init__(self, *args, **kwargs):
    super(OnlyUserForm, self).__init__(*args, **kwargs)

  nome = forms.CharField(max_length=40,label="Nome",required=True)
  email = forms.EmailField(max_length=40,label="Email",required=True)
  password = forms.CharField(widget=PasswordInput(render_value=True),max_length=100,label='Senha')
  confirm_password = forms.CharField(widget=PasswordInput(render_value=True),max_length=100,label='Confirmar Senha')
  edit = forms.IntegerField(widget = HiddenInput())

  def clean(self):
    cleaned_data = self.cleaned_data
    password = cleaned_data.get("password")
    confirm_password = cleaned_data.get("password2")

    if password != confirm_password:
      self._errors["password"] = self.error_class([u"As senhas digitadas são diferentes."])
      self._errors["password2"] = self.error_class([u"As senhas digitadas são diferentes."])

    try:
      email = cleaned_data['email']
    except:
      email = None

    edit = cleaned_data['edit']

    ue = User.objects.filter(email=email)

    if ue[0].id != edit:
      self._errors["email"] = self.error_class([u"Email já cadastrado."])
      raise forms.ValidationError("not unique")


    return cleaned_data