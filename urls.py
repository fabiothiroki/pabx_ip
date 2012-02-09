# -*- coding:utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login,logout,logout_then_login,password_reset,password_reset_done,password_reset_complete,password_reset_confirm

from django.contrib import admin
admin.autodiscover()


handler500 = "pinax.views.server_error"


urlpatterns = patterns("",
    url(r"^$", login_required(direct_to_template), {
        "template": "base.html",
    }, name=u"Página Inicial"),
    url(r"^admin/", include(admin.site.urls)),

	url(r'^accounts/login/$', 'accounts.views.login' ),
    url(r'^accounts/logout/$', 'accounts.views.logout'),
    url(r'^accounts/settings/$', 'accounts.views.settings'),
    url(r'^accounts/create/$', 'accounts.views.create'),
    url(r'^accounts/edit/(\d+)/$','accounts.views.edit'),
    url(r'^accounts/remove/(\d+)/$','accounts.views.delete'),
    url(r'^accounts/editself/$','accounts.views.edit_self'),

)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
