# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required,user_passes_test
from django.template.context import Context,RequestContext

from accounts.decorators import is_admin
from smtp.models import server
from smtp.forms import smtpform

@login_required
@is_admin
def index(request):
    highlight = 'smtp'
    title = 'Servidor SMTP'

    columns = ["Endereço","Porta","Usuário"]
    show = []

    if server.objects.all().exists() == True:
        s = server.objects.all()[0]
        url = s.url
        port = s.port
        username = s.username

        show.append([url,port,username])

    add_button = '<a class="btn btn-primary" href="/smtp/configure">Configurar Servidor SMTP</a>'

    empty_message = "O serviço de envio de emails não está configurado."

    return render_to_response('crud.html',locals(),context_instance=RequestContext(request))

@login_required
@is_admin
def configure(request):

    if request.method == 'POST':
        form = smtpform(request.POST)

        if form.is_valid():
            highlight = 'smtp'
            title = 'Servidor SMTP configurado com sucesso'
            cancel_link = '/smtp/index'

            try:
                s = server.objects.all()[0]
            except:
                s = server()

            s.url = form.cleaned_data['url']
            s.port = form.cleaned_data['port']
            s.username = form.cleaned_data['username']
            s.password = form.cleaned_data['password']

            s.save()

            return render_to_response("form_success.html",locals(),context_instance=RequestContext(request),)
        else:
            highlight = 'smtp'
            title = 'Configurar servidor SMTP'

            return render_to_response('form_create.html',locals(),context_instance=RequestContext(request))
    else:

        count = server.objects.all().count()

        if count != 0:

            s = server.objects.all()[0]

            form=smtpform(initial={
                'url':s.url,
                'port':s.port,
                'username':s.username,
                'password':s.password,
                'password2':s.password,
            })
        else:
            form = smtpform()

        highlight = 'smtp'
        title = 'Configurar servidor SMTP'
        cancel_link = '/smtp/index'

        return render_to_response('form_create.html',locals(),context_instance=RequestContext(request))