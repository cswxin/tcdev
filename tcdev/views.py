#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os, sys
sys.path.insert(0, os.path.abspath(os.curdir))

from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import logging

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login as jlogin, logout as jlogout
from service import _user
import requests
import json
import traceback


logger = logging.getLogger('logger')

@csrf_exempt
def login(request):
    redirect_to = request.REQUEST.get("next", reverse('index'))
    try:
            if request.method == "POST":
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = auth.authenticate(username=username, password=password)
                if user is not None and user.is_active:
                    auth.login(request, user)
                    logger.debug("[user login] %s login ok." % (username))
                    return HttpResponseRedirect(redirect_to)

                if user and not user.is_active:
                    error_msg = u'账号未激活'
                else:
                    error_msg = u'账号或密码错误，请重新输入'
                logger.error(error_msg)
            else:
                if request.user.is_authenticated():
                    return HttpResponseRedirect(redirect_to)
                return render_to_response("login.html", locals())
    except Exception, e:
        error = traceback.format_exc()
        logger.error(error)
        print error
    return HttpResponseRedirect(redirect_to)


@csrf_exempt
def logout(request):
#     sdict = {}
    jlogout(request)
    response = HttpResponseRedirect('/index/')
    return response
#     sdict['result'] = 1
#     return HttpResponse(json.dumps(sdict), content_type="application/json")