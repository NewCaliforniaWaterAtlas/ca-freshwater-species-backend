from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from api.resources import *

v1_api = Api(api_name='v1')
v1_api.register(SourceResource())

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    (r'api/doc/', include('tastypie_swagger.urls', namespace='tastypie_swagger')),
    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),
)
