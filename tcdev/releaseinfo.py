# encoding:utf-8

import os

REL_SITE_ROOT = os.path.dirname(os.path.abspath(__file__))

REL_STATIC_ROOT = os.path.join(REL_SITE_ROOT, 'static').replace('\\', '/')

REL_DEBUG = True

DATABASE_ENGINE = 'django.db.backends.mysql'
DATABASE_NAME = 'tcdev'
# DATABASE_USER = 'root'
# DATABASE_PASSWORD = 'snailgame@123'
# DATABASE_HOST = '10.90.12.236'
DATABASE_USER = 'root'
DATABASE_PASSWORD = 'root'
DATABASE_HOST = '127.0.0.1'
DATABASE_PORT = '3306'

# REL_ROOT_PATH = 'http://124.202.142.136:88'
REL_ROOT_PATH = 'http://127.0.0.1:80'
REL_MEDIA_URL = '%s/file/' % REL_ROOT_PATH
REL_MEDIA_ROOT = os.path.join(REL_SITE_ROOT, 'file')
REL_UPLOAD_ROOT = os.path.join(REL_SITE_ROOT, 'upload')



LOGIN_URL = '/login/'


SPECIAL_USERS = ['wx', 'hmx']

