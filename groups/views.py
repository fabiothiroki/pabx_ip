# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required,user_passes_test
from django.template.context import Context,RequestContext

from pabx_ip.accounts.models import UserProfile
from pabx_ip.accounts.decorators import is_admin

from groups.forms import *
from groups.models import *

@login_required
@is_admin
def index(request):
	highlight = 'groups'
	title = 'Grupos de usuários'

	columns = ["Nome do Grupo","Ação"]
	show = []

	if Group.objects.all().exists() == True:
		for g in Group.objects.all():
			name = g.name

			action = '<p align="center">'
			action += "<a class='btn' href='/groups/edit/"+str(g.id)+"'><i class='icon-pencil'></i>Editar</a>"
			action += ' <a class="btn btn-danger" href="/groups/remove/'+str(g.id)+'"><i class="icon-trash icon-white"></i>Remover</a>'
			action += ' '
			action += '</p>'

			show.append([name,action])

	add_button = '<a class="btn btn-primary" href="/groups/create"><i class="icon-plus icon-white"></i>Adicionar Grupo</a>'
	empty_message = "Nenhum grupo adicionado."

	return render_to_response('crud.html',locals(),context_instance=RequestContext(request))

@login_required
@is_admin
def create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():

            save_or_update(form)

            title = "Grupo adicionado com sucesso"
            highlight = "groups"
            cancel_link = "/groups/index/"
            cancel_name = "Grupos de Usuários"

            return render_to_response("form_success.html",locals(),context_instance=RequestContext(request),)
        else:
            title = "Adicionar Grupo"
            highlight = "groups"
            cancel_link = "/groups/index/"
            return render_to_response("form_create.html",locals(),context_instance=RequestContext(request),)
    else:
        title = "Adicionar Grupo"
        highlight = "groups"
        cancel_link = "/groups/index/"
        form = GroupForm(initial={'edit':0})

        return render_to_response("form_create.html",locals(),context_instance=RequestContext(request),)