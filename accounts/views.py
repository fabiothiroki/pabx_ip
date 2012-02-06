# -*- coding:utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.template.context import Context,RequestContext

def login(request):

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)

            request.session['username'] = username

            return render_to_response('base.html',locals(),context_instance=RequestContext(request))

        else:
            # Show an error page
            erro = u"Usuário ou senha incorretos."
            return render_to_response('login.html',locals(),context_instance=RequestContext(request))

    else:
        return render_to_response('login.html',locals(),context_instance=RequestContext(request))