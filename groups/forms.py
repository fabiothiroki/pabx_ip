# -*- coding: utf-8 -*-
from groups.models import Group
from django import forms
from django.forms.widgets import *

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group

    def __init__(self, *args, **kwargs):
      super(GroupForm, self).__init__(*args, **kwargs)
      self.fields['can_call_ramal'].widget.attrs['disabled'] = 'disabled'
      self.fields['can_call_emergency'].widget.attrs['disabled'] = 'disabled'