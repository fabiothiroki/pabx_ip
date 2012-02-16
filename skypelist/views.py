# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required,user_passes_test
from django.template.context import Context,RequestContext

from accounts.decorators import is_admin
from skypelist.models import skypeuser
from skypelist.forms import skypeform

@login_required
@is_admin
def index(request):
    highlight = 'skypelist'
    title = 'Lista de contatos Skype'

    columns = ["Usuário Skype","Ramal Skype", "Ação"]
    show = []

    if skypeuser.objects.all().exists() == True:

        users = skypeuser.objects.all()

        for u in users:

            action = '<p align="center">'
            action += "<a class='btn' href='/skypelist/edit/"+str(u.id)+"'><i class='icon-pencil'></i>Editar</a>"
            action += ' <a class="btn btn-danger" href="/skypelist/remove/'+str(u.id)+'"><i class="icon-trash icon-white"></i>Remover</a>'
            action += '</p>'

            show.append([u.username,u.ramal,action])

    add_button = '<a class="btn btn-primary" href="/skypelist/create"><i class="icon-plus icon-white"></i>Adicionar Contato</a>'
    empty_message = "Não existe nenhum contato cadastrado."

    return render_to_response('crud.html',locals(),context_instance=RequestContext(request))

@login_required
@is_admin
def create(request):
    if request.method == 'POST':
        form = skypeform(request.POST)

        if form.is_valid():
            highlight = 'skypelist'
            title = 'Usuário Skype adicionado com sucesso'
            cancel_link = '/skypelist/index'

            form.save()

            return render_to_response("form_success.html",locals(),context_instance=RequestContext(request),)
        else:
            highlight = 'skypelist'
            title = 'Adicionar contato Skype'
            cancel_link = '/skypelist/index'
            return render_to_response('form_create.html',locals(),context_instance=RequestContext(request))
    else:

        form = skypeform()

        highlight = 'skypelist'
        title = 'Adicionar contato Skype'
        cancel_link = '/skypelist/index'

        return render_to_response('form_create.html',locals(),context_instance=RequestContext(request))

@login_required
@is_admin
def edit(request,offset):

    try:
        su = skypeuser.objects.get(pk=offset)
    except:
        raise PermissionDenied


    if request.method == 'POST':
        form = skypeform(request.POST,instance=su)

        if form.is_valid():
            highlight = 'skypelist'
            title = 'Usuário Skype editado com sucesso'
            cancel_link = '/skypelist/index'

            form.save()

            return render_to_response("form_success.html",locals(),context_instance=RequestContext(request),)

        else:
            highlight = 'skypelist'
            title = 'Editar contato Skype'
            cancel_link = '/skypelist/index'

            return render_to_response('form_create.html',locals(),context_instance=RequestContext(request))

    else:

        
        form = skypeform(instance = su)

        highlight = 'skypelist'
        title = 'Editar contato Skype'
        cancel_link = '/skypelist/index'

        return render_to_response('form_create.html',locals(),context_instance=RequestContext(request))