# -*- coding:utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.template.context import Context,RequestContext
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required,user_passes_test

from pabx_ip.accounts.models import UserProfile
from pabx_ip.accounts.decorators import is_admin
from accounts.forms import UserForm

def login(request):

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)

            if (username == 'root'):
                request.session["is_admin"] = True
            else:
                up = UserProfile.objects.get(profile=user.id)

                if up.admin == True:
                    request.session["is_admin"] = True
                else:
                    request.session["is_admin"] = False

            request.session['username'] = username

            title = u"Página Inicial"
            highlight = ''

            return render_to_response('base.html',locals(),context_instance=RequestContext(request))

        else:
            # Show an error page
            erro = u"Usuário ou senha incorretos."
            return render_to_response('login.html',locals(),context_instance=RequestContext(request))

    else:
        return render_to_response('login.html',locals(),context_instance=RequestContext(request))

@login_required
def logout(request):
    return logout_then_login(request)

@login_required
@is_admin
def settings(request):

    title = "Gerenciar Usuários"
    highlight = "accounts"

    columns = ["Nome","Ramal","Email","Tipo",u"Ação"]

    users = User.objects.all()

    userdict = []
    show = []
    for u in users:

        try:
            if u.username != 'root':
                up = UserProfile.objects.get(profile=u.id)

                if up.admin == True:
                    admin = 'Administrador'
                else:
                    admin = 'Usuário'

                # Somente o usuario root edita outros admins
                if request.session["username"] != 'root' and up.admin == True and u.username != request.session["username"]:
                    continue

                action = '<p align="center">'
                action += '<a class="btn" href="#"><i class="icon-pencil"></i>Editar</a>'
                action += ' <a class="btn btn-danger" href="#"><i class="icon-trash icon-white"></i>Remover</a>'
                action += '</p>'

                userdict = [u.first_name,up.ramal,u.email,admin,action]

                show.append(userdict)
        except Exception as err:
            print err
            pass

    add_button = '<a class="btn btn-primary" href="/accounts/create"><i class="icon-plus icon-white"></i>Adicionar Usuário</a>'

    return render_to_response('crud.html',locals(),context_instance=RequestContext(request))

@login_required
@is_admin
def create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():

            save_or_update(form)

            title = "Usuário adicionado com sucesso"
            highlight = "accounts"
            cancel_link = "/accounts/settings/"
            cancel_name = "Gerenciar Usuários"

            return render_to_response("form_success.html",locals(),context_instance=RequestContext(request),)
        else:
            title = "Adicionar Usuário"
            highlight = "accounts"
            cancel_link = "/accounts/settings/"
            return render_to_response("form_create.html",locals(),context_instance=RequestContext(request),)
    else:
        title = "Adicionar Usuário"
        highlight = "accounts"
        cancel_link = "/accounts/settings/"
        form = UserForm()

        return render_to_response("form_create.html",locals(),context_instance=RequestContext(request),)

@login_required
@is_admin
def edit(request,offset):

    user = User.objects.get(pk=int(offset))
    profile = UserProfile.objects.get(profile=int(offset))

    if request.method == 'POST':
        form = UserForm(request.POST)

        return render_to_response("form_success.html",locals(),context_instance=RequestContext(request),)
    else:
        form = UserForm()


        
        return render_to_response("form_success.html",locals(),context_instance=RequestContext(request),)

def save_or_update(form,user=None,profile=None):

    nome = form.cleaned_data['nome']
    email = form.cleaned_data['email']
    password = form.cleaned_data['password']
    ramal = form.cleaned_data['ramal']
    admin = form.cleaned_data['admin']
    can_call_fix = form.cleaned_data['can_call_fix']
    can_call_mobile = form.cleaned_data['can_call_mobile']
    can_call_ddd = form.cleaned_data['can_call_ddd']
    can_call_ddi = form.cleaned_data['can_call_ddi']
    can_call_0800 = form.cleaned_data['can_call_0800']
    can_call_0300 = form.cleaned_data['can_call_0300']

    if (user == None):
        user = User()
    else:
        pass
    user.first_name = nome
    user.username = email
    user.email = email
    user.set_password(password)
    user.save()

    if (profile == None):
        profile = UserProfile()
    else:
        pass
    profile.profile = user
    profile.ramal = ramal
    profile.admin = admin
    profile.can_call_fix = can_call_fix
    profile.can_call_mobile = can_call_mobile
    profile.can_call_ddd = can_call_ddd
    profile.can_call_ddi = can_call_ddi
    profile.can_call_0800 = can_call_0800
    profile.can_call_0300 = can_call_0300
    profile.save()