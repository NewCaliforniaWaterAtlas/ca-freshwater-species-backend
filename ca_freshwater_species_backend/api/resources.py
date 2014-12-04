from tastypie import fields
from tastypie.resources import ModelResource
from ca_freshwater_species_backend.models import *


class OriginResource(ModelResource):
    class Meta:
        queryset = Origin.objects.all()
        resource_name = 'origin'
        allowed_methods = ['get']
        excludes = ['id', 'org_id']


class ObservationTypeResource(ModelResource):
    class Meta:
        queryset = ObservationType.objects.all()
        resource_name = 'observation_type'
        allowed_methods = ['get']
        excludes = ['id', 'obs_typ_id']


class SourceResource(ModelResource):
    class Meta:
        queryset = Source.objects.all()
        resource_name = 'source'
        allowed_methods = ['get']
        excludes = ['source_id']


class HabitatUsageResource(ModelResource):
    class Meta:
        queryset = HabitatUsage.objects.all()
        resource_name = 'habitat_usage'
        allowed_methods = ['get']
        excludes = ['id', 'hab_usage_id']


class ElementResource(ModelResource):
    class Meta:
        queryset = Element.objects.all()
        resource_name = 'element'
        allowed_methods = ['get']
        limit = 0
        max_limit = 0
        filtering = {
            'group_field': ('iexact')
        }
        includes = [
            'common',
            'elm_comnam',
            'elm_scinam',
            'endemic',
            'endemism_comment',
            'extinct',
            'family',
            'genus',
            'group_field',
            'kingdom',
            'listed',
            'mgtag_list',
            'not_evaluated',
            'ns_endemic',
            'other_endemic',
            'other_list',
            'phylum',
            'resource_uri',
            's_rank',
            'safit_endemic',
            'sensitive_fam',
            'species',
            'tax_class',
            'tax_list',
            'tax_order',
            'vulnerable',
        ]


class AuVElmResource(ModelResource):
    element = fields.ToOneField(ElementResource, 'element', full=True)
    observation_type = fields.ToOneField(ObservationTypeResource, 'observation_type', full=True)
    source = fields.ToOneField(SourceResource, 'source', full=True)

    class Meta:
        queryset = AuVElm.objects.all()
        resource_name = 'au_v_elm'
        allowed_methods = ['get']
        excludes = ['id']

