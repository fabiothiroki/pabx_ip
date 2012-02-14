# -*- coding:utf8 -*-

from django import forms
from django.forms.widgets import *

from smtp.models import server

class smtpform(forms.ModelForm):
	class Meta:
		model = server

	def __init__(self, *args, **kwargs):
	  super(smtpform, self).__init__(*args, **kwargs)

	password = forms.CharField(widget=PasswordInput(render_value=True),max_length=100,label='Senha',required=True)
	password2 = forms.CharField(widget=PasswordInput(render_value=True),max_length=100,label='Confirmação de Senha',required=True)

	def clean(self):
	  cleaned_data = self.cleaned_data
	  password = cleaned_data.get("password")
	  confirm_password = cleaned_data.get("password2")

	  if password != confirm_password:
	    self._errors["password"] = self.error_class([u"As senhas digitadas são diferentes."])
	    self._errors["password2"] = self.error_class([u"As senhas digitadas são diferentes."])

	  return cleaned_data