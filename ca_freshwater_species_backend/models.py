# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.contrib.gis.db import models


class AuVElm(models.Model):
    id = models.BigIntegerField(primary_key=True)
    object_id = models.IntegerField(blank=True, null=True)
    huc_12 = models.CharField(max_length=12, blank=True)
    hab_usage_id = models.IntegerField(blank=True, null=True)
    obs_typ_id = models.IntegerField(blank=True, null=True)
    fmt_id = models.IntegerField(blank=True, null=True)
    org_id = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    elm_id = models.IntegerField(blank=True, null=True)
    elm_type_id = models.IntegerField(blank=True, null=True)
    quality = models.CharField(max_length=16, blank=True)
    amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_v_elm'


class Elements(models.Model):
    id = models.BigIntegerField(primary_key=True)
    object_id = models.IntegerField(blank=True, null=True)
    elm_scinam = models.CharField(max_length=64, blank=True)
    elm_comnam = models.CharField(max_length=64, blank=True)
    group_field = models.CharField(db_column='group_', max_length=32, blank=True)  # Field renamed because it ended with '_'.
    fwa_v1 = models.IntegerField(blank=True, null=True)
    tax_list = models.CharField(max_length=32, blank=True)
    g_rank = models.CharField(max_length=16, blank=True)
    s_rank = models.CharField(max_length=32, blank=True)
    elm_scin_1 = models.CharField(max_length=64, blank=True)
    elm_scin_2 = models.CharField(max_length=64, blank=True)
    elm_scin_3 = models.CharField(max_length=64, blank=True)
    elm_scin_4 = models.CharField(max_length=64, blank=True)
    kingdom = models.CharField(max_length=32, blank=True)
    phylum = models.CharField(max_length=32, blank=True)
    tax_class = models.CharField(max_length=32, blank=True)
    tax_order = models.CharField(max_length=32, blank=True)
    family = models.CharField(max_length=32, blank=True)
    genus = models.CharField(max_length=32, blank=True)
    species = models.CharField(max_length=32, blank=True)
    subsp_var = models.CharField(max_length=32, blank=True)
    kingdom_id = models.IntegerField(blank=True, null=True)
    phylum_id = models.IntegerField(blank=True, null=True)
    tax_class_i = models.IntegerField(blank=True, null=True)
    tax_order_i = models.IntegerField(blank=True, null=True)
    family_id = models.IntegerField(blank=True, null=True)
    genus_id = models.IntegerField(blank=True, null=True)
    species_id = models.IntegerField(blank=True, null=True)
    elm_id = models.IntegerField(blank=True, null=True)
    other_id = models.IntegerField(blank=True, null=True)
    sensitive_fam = models.CharField(max_length=32, blank=True)
    ns_endemic = models.IntegerField(blank=True, null=True)
    safit_endemic = models.IntegerField(blank=True, null=True)
    other_endemic = models.IntegerField(blank=True, null=True)
    endemism_comment = models.TextField(blank=True)
    fed_list = models.CharField(max_length=64, blank=True)
    state_list = models.CharField(max_length=64, blank=True)
    other_list = models.CharField(max_length=64, blank=True)
    mgtag_list = models.CharField(max_length=32, blank=True)
    listed = models.NullBooleanField()
    vulnerable = models.NullBooleanField()
    endemic = models.NullBooleanField()
    common = models.NullBooleanField()
    not_evaluated = models.NullBooleanField()
    extinct = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'elements'


class HabitatUsage(models.Model):
    id = models.BigIntegerField(primary_key=True)
    object_id = models.IntegerField(blank=True, null=True)
    hab_usage_id = models.IntegerField(blank=True, null=True)
    hab_usage_name = models.CharField(max_length=32, blank=True)

    class Meta:
        managed = False
        db_table = 'habitat_usage'


class ObservationType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    object_id = models.IntegerField(blank=True, null=True)
    obs_typ_id = models.IntegerField(blank=True, null=True)
    obs_typ_name = models.CharField(max_length=64, blank=True)
    range_obs = models.CharField(max_length=32, blank=True)
    current_other = models.CharField(max_length=32, blank=True)

    class Meta:
        managed = False
        db_table = 'observation_type'


class Origin(models.Model):
    id = models.BigIntegerField(primary_key=True)
    object_id = models.IntegerField(blank=True, null=True)
    org_id = models.IntegerField(blank=True, null=True)
    org_name = models.CharField(max_length=32, blank=True)

    class Meta:
        managed = False
        db_table = 'origin'


class Source(models.Model):
    id = models.BigIntegerField(primary_key=True)
    object_id = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    source_name = models.CharField(max_length=256, blank=True)
    sourcegrp_name = models.CharField(max_length=64, blank=True)
    use_agree = models.TextField(blank=True)
    permission_request_needed = models.CharField(max_length=64, blank=True)
    permission_contact_name = models.CharField(max_length=32, blank=True)
    permission_contact_email = models.CharField(max_length=64, blank=True)
    permission_status = models.TextField(blank=True)
    permission = models.CharField(max_length=32, blank=True)
    comment_id = models.IntegerField(blank=True, null=True)
    citation = models.TextField(blank=True)
    weblink = models.CharField(max_length=128, blank=True)
    pre_release_review = models.CharField(max_length=8, blank=True)
    aggregator = models.CharField(max_length=32, blank=True)
    count_huc12s = models.IntegerField(blank=True, null=True)
    count_elm_ids = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'source'