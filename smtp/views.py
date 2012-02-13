# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required,user_passes_test
from django.template.context import Context,RequestContext

from pabx_ip.accounts.decorators import is_admin
from smtp.models import server

@login_required
@is_admin
def index(request):
	highlight = 'smtp'
	title = 'Servidor SMTP'

	columns = ["Endereço","Porta","Usuário"]
	show = []

	count = server.objects.all().count()

	if count != 0:
		url = server[0].url
		port = server[0].port
		username = server[0].username

		show.append([])



	add_button = '<a class="btn btn-primary" href="/smtp/configure">Configurar Servidor SMTP</a>'

	empty_message = "O serviço de envio de emails não está configurado."

	return render_to_response('crud.html',locals(),context_instance=RequestContext(request))