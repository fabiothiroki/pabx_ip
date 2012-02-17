# -*- coding:utf8 -*-

from django import forms
from django.forms.widgets import *

from skypelist.models import skypeuser
from accounts.models import UserProfile

class skypeform(forms.ModelForm):
    class Meta:
        model = skypeuser

    edit = forms.IntegerField(widget = HiddenInput())

    def __init__(self, *args, **kwargs):
      super(skypeform, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = self.cleaned_data

        ramal = cleaned_data.get("ramal")
        username = cleaned_data.get("username")
        userid = cleaned_data.get("edit")

        # valida edição de usuario para outro ramal skype igual
        if skypeuser.objects.filter(ramal=ramal).exists() == True: # existe um ramal igual
            if userid:
                if skypeuser.objects.get(ramal=ramal).id != userid: # existe um ramal igual para outro usuario
                    self._errors["ramal"] = self.error_class([u"Ramal já existente."])
            else:
                self._errors["ramal"] = self.error_class([u"Ramal já existente."]) # criação de usuario com msm ramal skype

        if UserProfile.objects.filter(ramal=ramal).exists() == True: # existe um ramal nao skype com numero igual
            self._errors["ramal"] = self.error_class([u"Ramal já existente."])


        if skypeuser.objects.filter(username=username).exists() == True:
            if skypeuser.objects.get(username=username).id != userid:
                self._errors["username"] = self.error_class([u"Usuário Skype já existente."])

        return cleaned_data