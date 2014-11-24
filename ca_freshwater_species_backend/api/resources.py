from tastypie import fields
from tastypie.resources import ModelResource
from ca_freshwater_species_backend.models import *


class SourceResource(ModelResource):
    class Meta:
        queryset = Source.objects.all()
        allowed_methods = ['get']


class OriginResource(ModelResource):
    class Meta:
        queryset = Origin.objects.all()
        allowed_methods = ['get']


class ObservationTypeResource(ModelResource):
    class Meta:
        queryset = ObservationType.objects.all()
        allowed_methods = ['get']


class HabitatUsageResource(ModelResource):
    class Meta:
        queryset = HabitatUsage.objects.all()
        allowed_methods = ['get']


class ElementResource(ModelResource):
    class Meta:
        queryset = Element.objects.all()
        resource_name = 'element'
        allowed_methods = ['get']


class AuVElmResource(ModelResource):
    element = fields.ToOneField(ElementResource, 'element')

    class Meta:
        queryset = AuVElm.objects.all()
        allowed_methods = ['get']
