# -*- coding:utf-8 -*-
import smtplib
import bz2
import base64
from email.mime.text import MIMEText

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.template.context import Context,RequestContext
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.exceptions import PermissionDenied
from django.conf import settings

from pabx_ip.accounts.models import UserProfile
from pabx_ip.accounts.decorators import is_admin
from accounts.forms import *
from smtp.models import server

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
            request.session['user_id'] = user.id
            request.session['name'] = user.first_name

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

        # 1) Na tabela de exibição de usuários, não é para ser exibido o usuário 'root' pois não deve ser possível editá-lo,
        # visto que ele é somente o super-admin do sistema.
        # 2) Não será exibido usuários Administradores para um Administrador logado, a visualização/edição/remoção de outros
        # Administradores só poderá ser feita pelo usuário root

        try:
            if u.username != 'root':
                up = UserProfile.objects.get(profile=u.id)

                if up.admin == True:
                    if request.session['username'] != 'root':
                        continue
                    else:
                        admin = 'Administrador'
                else:
                    admin = 'Usuário'

                # Somente o usuario root edita outros admins
                if request.session["username"] != 'root' and up.admin == True and u.username != request.session["username"]:
                    continue

                action = '<p align="center">'
                action += "<a class='btn' href='/accounts/edit/"+str(u.id)+"'><i class='icon-pencil'></i>Editar</a>"
                action += ' <a class="btn btn-danger" href="/accounts/remove/'+str(u.id)+'"><i class="icon-trash icon-white"></i>Remover</a>'
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
        form = UserForm(initial={'edit':0})

        return render_to_response("form_create.html",locals(),context_instance=RequestContext(request),)

@login_required
@is_admin
def edit(request,offset):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():

            user = User.objects.get(pk=int(offset))
            profile = UserProfile.objects.get(profile=int(offset))

            save_or_update(form,user,profile)

            title="Usuário Editado com sucesso"
            highlight = "accounts"
            cancel_link = "/accounts/settings/"
            cancel_name = "Gerenciar Usuários"

            return render_to_response("form_success.html",locals(),context_instance=RequestContext(request),)
        else:

            return render_to_response("form_create.html",locals(),context_instance=RequestContext(request),)
    else:
        title = "Editar Usuário"
        highlight = "accounts"
        cancel_link = "/accounts/settings/"

        try:
            user = User.objects.get(pk=int(offset))
            profile = UserProfile.objects.get(profile=int(offset))
        except:
            raise PermissionDenied

        if (request.session['username'] != 'root'):
            if (profile.admin == True):
                if request.session['user_id'] != int(offset):
                    raise PermissionDenied

        form = UserForm(initial={
            'nome':user.first_name,
            'email':user.email,
            'password':user.password,
            'password2':user.password,
            'ramal':profile.ramal,
            'admin':profile.admin,
            'group':profile.group,
            'edit':int(offset),
        })

        
        return render_to_response("form_create.html",locals(),context_instance=RequestContext(request),)

@login_required
@is_admin
def delete(request,offset):
    if request.method == 'POST':

        user = User.objects.get(pk=int(offset))
        profile = UserProfile.objects.get(profile=int(offset))

        user.delete()
        profile.delete()

        title=u"Usuário Removido com sucesso"
        highlight = "accounts"
        cancel_link = "/accounts/settings/"
        cancel_name = u"Gerenciar Usuários"

        return render_to_response("form_success.html",locals(),context_instance=RequestContext(request),)

    else:
        try:
            user = User.objects.get(pk=int(offset))
            profile = UserProfile.objects.get(profile=int(offset))
        except:
            raise PermissionDenied

        if request.session['username'] != 'root':
            if profile.admin == True:
                raise PermissionDenied

        title = u"Remover Usuário"
        highlight = "accounts"
        cancel_link = "/accounts/settings/"
        what = "o usuário "+str(user.email)

        return render_to_response("form_delete.html",locals(),context_instance=RequestContext(request),)

@login_required
def edit_self(request):
    if request.method == 'POST':
        form = OnlyUserForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=int(request.session['user_id']))

            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user.first_name = nome
            if user.username != 'root':
                user.username = email
            user.email = email

            if user.password != password:
                user.set_password(password)
            user.save()

            title="Usuário Editado com sucesso"
            cancel_link = "/"

        return render_to_response("form_success.html",locals(),context_instance=RequestContext(request),)
    else:
        
        if request.session['is_admin']:
            if request.session['username'] != 'root':
                return HttpResponseRedirect("/accounts/edit/"+str(request.session['user_id']))
            else:
                user = User.objects.get(pk=int(request.session['user_id']))

                # only user form
                form = OnlyUserForm(initial={
                    'nome':user.first_name,
                    'email':user.email,
                    'password':user.password,
                    'password2':user.password2,
                    'edit':user.id
                })

                title="Editar Usuário"
                cancel_link = "/"

                return render_to_response("form_create.html",locals(),context_instance=RequestContext(request),)
        else:
            # only user form
            form = OnlyUserForm(initial={
                'nome':user.first_name,
                'email':user.email,
                'password':user.password,
                'password2':user.password2,
                'edit':user.id
            })

            title="Usuário Editado com sucesso"
            cancel_link = "/"
            return render_to_response("form_create.html",locals(),context_instance=RequestContext(request),)

def save_or_update(form,user=None,profile=None):

    # 1) Esse método foi criado como forma de refatoração do código, visto que ele é usado similarmente na criação
    # e na edição de um usuário que não o próprio logado

    nome = form.cleaned_data['nome']
    email = form.cleaned_data['email']
    password = form.cleaned_data['password']
    ramal = form.cleaned_data['ramal']
    admin = form.cleaned_data['admin']
    group = form.cleaned_data['group']

    if (user == None):
        user = User()
    else:
        pass
    user.first_name = nome
    user.username = email
    user.email = email

    if user.password != password:
        user.set_password(password)
    
    user.save()

    try:
        if (profile == None):
            profile = UserProfile()
        else:
            pass
        profile.profile = user
        profile.ramal = ramal
        profile.admin = admin
        profile.group = group

        # 1) Aqui salvamos o password numa outra tabela diferente do sistema Auth nativo do Django, para que seja possível
        # a recuperação dessa senha depois
        if user.password != password:
            profile.passw = encrypt(password)

        profile.save()
    except Exception as err:
        user.delete()
        print err

def password_reset(request):

    if request.method == 'POST':
        form = PassResetForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']

            if server.objects.all().exists() == True:

                s = server.objects.all()[0]

                u = User.objects.get(email=email)
                up = UserProfile.objects.get(profile=u)
                p = unencrypt(up.passw)

                msg = MIMEText('Sua senha:'+str(p))
                msg['Subject'] = 'Recuperação da senha'
                msg['From'] = s.username
                msg['To'] = email

                serve = smtplib.SMTP(s.url+':'+str(s.port))
                serve.starttls()  
                serve.login(s.username,s.password)  
                serve.sendmail(s.username, [email], msg.as_string())  
                serve.quit() 

                le_message = "A senha foi enviada para o email indicado."

            else:
                le_message = "A senha não pôde ser enviada para o email indicado. Entre em contato com o administrador do sistema para recuperar sua senha."


            return render_to_response("accounts/templates/password_reset_success.html",locals(),context_instance=RequestContext(request),)
        else:
            return render_to_response("accounts/templates/password_reset_form.html",locals(),context_instance=RequestContext(request),)

    else:
        form = PassResetForm()

        return render_to_response("accounts/templates/password_reset_form.html",locals(),context_instance=RequestContext(request),)

def encrypt(plaintext):
    encrypted_password = base64.b64encode(plaintext)

    return encrypted_password

def unencrypt(encrypted_password):
    return base64.b64decode(str(encrypted_password)) 