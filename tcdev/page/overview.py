# -- encoding=utf-8 --
import os
import sys

sys.path.insert(0, os.path.abspath(os.curdir))

from django.contrib import auth
from utils.decorator import render_to, login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.transaction import commit_on_success
from django.http import HttpResponse
import json
import datetime
import logging
import traceback
from releaseinfo import SPECIAL_USERS
from utils.WXBizMsgCrypt import WXBizMsgCrypt

logger = logging.getLogger("myforms_logger")


@csrf_exempt
@render_to('index.html')
def index(request):
    return locals()


@csrf_exempt
@render_to('register.html')
def register(request):
    return locals()

@csrf_exempt
@render_to("login.html")
def login(request):
    if request.method == 'POST':
        sdict = {'result': 0}
        username = request.POST.get('username')
        password = request.POST.get('password')
  
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            logger.debug("[user login] %s login ok." % (username))
            sdict['result'] = 1
  
        return HttpResponse(json.dumps(sdict), content_type="application/json")
    else:
        return locals()
        

@login_required
@csrf_exempt
@render_to("perm.html")
def perm(request):
    return locals()


@csrf_exempt
def receive(request):
    token = "spamtest"
    encodingAESKey = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFG"
    appid = "wx2c2769f8efd9abc2"
    
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')
    msg_sign = request.GET.get('msg_signature')
    
    from_xml = json.loads(request.body)
    
    decrypt_test = WXBizMsgCrypt(token, encodingAESKey, appid)
    ret , decryp_xml = decrypt_test.DecryptMsg(from_xml, msg_sign, timestamp, nonce)
    print ret 
    print decryp_xml

    return HttpResponse("success", content_type="application/json")

from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^index/$', index, name='index'),
                       url(r'^register/$', register, name='register'),
                       url(r'^login/$', login, name='login'),
                       url(r'^perm/$', perm, name='perm'),
                       url(r'^receive/$', receive, name='receive'),
                       )
