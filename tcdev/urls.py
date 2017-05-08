from django.conf.urls import patterns, include, url
from settings import STATIC_ROOT, MEDIA_ROOT
# from views import login, logout
# from utils import util
from enums import enum_page
from views import login, logout
from django.utils.importlib import import_module

urlpatterns = patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),
    url(r'^file/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    
#     url(r'^$', login),
#     url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
#     url(r'^api/', include('api.urls')),

)

# urlpatterns.extend(util.urlpatterns)

for view in enum_page.PAGES:
    v = import_module("page." + view)
    urlpatterns.extend(v.urlpatterns)