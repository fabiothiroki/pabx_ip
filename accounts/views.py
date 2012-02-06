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
                
                userdict = [u.first_name,up.ramal,u.email,admin,""]

                show.append(userdict)
        except Exception as err:
            print err
            pass

    return render_to_response('crud.html',locals(),context_instance=RequestContext(request))