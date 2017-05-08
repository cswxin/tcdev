#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.abspath(os.curdir))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

import django
django.setup()

import settings
from django.db.transaction import commit_on_success
from service import _user
import json
import datetime

def add_users():
    for account in ['15106203986', '15106203981']:
        u, create = _user.get_or_create_user_by_params(username=account)
#             if create:
        u.set_password('123456')
        u.first_name = account
#             if cellphone:
#                 u.last_name = cellphone
            
        if account in ['15106203986', '15106203981']:
            u.is_superuser = True
        # print 'add user:', u
        u.save()

if __name__ == '__main__':
    add_users()