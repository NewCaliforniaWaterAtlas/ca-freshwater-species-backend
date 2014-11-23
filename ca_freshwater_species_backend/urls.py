from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
# from django.views.generic import TemplateView
from tastypie.api import Api
from api.resources import *

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(SourceResource())
v1_api.register(OriginResource())
v1_api.register(ObservationTypeResource())
v1_api.register(HabitatUsageResource())
v1_api.register(ElementResource())
v1_api.register(AuVElmResource())

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    (r'api/doc/', include('tastypie_swagger.urls', namespace='tastypie_swagger')),
)
