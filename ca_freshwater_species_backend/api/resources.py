from tastypie.resources import ModelResource
from ca_freshwater_species_backend.models import Source


class SourceResource(ModelResource):
    class Meta:
        queryset = Source.objects.all()
        allowed_methods = ['get']
