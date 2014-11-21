#!/usr/bin/env python

#
# Run this from the top level as
#
#    honcho run python wkg/data_loader.py 'subdirectory'
#

import os
import psycopg2
from petl import *
import argparse
from collections import OrderedDict

# get the subdirectory containing the .csv files from the command line and check that it exists.
#
parser = argparse.ArgumentParser(description='Import .csv files for the Freshwater Species Database.')
parser.add_argument('subdir', help="name of the database subdirectory (expected to be in 'wkg/')")
args = parser.parse_args()
if not os.path.exists(os.path.join('wkg', args.subdir)):
    print('Error: ' + args.subdir + " does not exist as a subdirectory of 'wkg/'.")
    exit()

# Set up the database connection
#
connection = psycopg2.connect(
    database=os.environ['DB'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'],
    host=os.environ['DB_HOST'],
)
cursor = connection.cursor()

# Origin: create, map, and load
#
cursor.execute("""
DROP TABLE IF EXISTS origin;
create table origin (
    id                          BIGSERIAL NOT NULL UNIQUE PRIMARY KEY,
    object_id                   INTEGER,
    org_id                      INTEGER,
    org_name                    VARCHAR(32)
);
""")
f = fromcsv(os.path.join('wkg', args.subdir, 'Origin.csv'))
f = rename(f, {
    'OBJECTID':                 'object_id',
    'Org_ID':                   'org_id',
    'Org_Name':                 'org_name',
})
todb(f, connection, 'origin')

# ObservationType: create, map, and load
#
cursor.execute("""
DROP TABLE IF EXISTS observation_type;
create table observation_type (
    id                          BIGSERIAL NOT NULL UNIQUE PRIMARY KEY,
    object_id                   INTEGER,
    obs_typ_id                  INTEGER,
    obs_typ_name                VARCHAR(64),
    range_obs                   VARCHAR(32),
    current_other               VARCHAR(32)
);
""")
f = fromcsv(os.path.join('wkg', args.subdir, 'ObservationType.csv'))
f = rename(f, {
    'OBJECTID':                 'object_id',
    'ObsTyp_ID':                'obs_typ_id',
    'ObsTyp_Name':              'obs_typ_name',
    'Range_Obs':                'range_obs',
    'Current_Other':            'current_other',
})
todb(f, connection, 'observation_type')

# Source: create, map, and load
#
cursor.execute("""
DROP TABLE IF EXISTS source;
create table source (
    id                          BIGSERIAL NOT NULL UNIQUE PRIMARY KEY,
    object_id                   INTEGER,
    source_id                   INTEGER,
    source_name                 VARCHAR(256),
    sourcegrp_name              VARCHAR(64),
    use_agree                   TEXT,
    permission_request_needed   VARCHAR(64),
    permission_contact_name     VARCHAR(32),
    permission_contact_email    VARCHAR(64),
    permission_status           TEXT,
    permission                  VARCHAR(32),
    comment_id                  INTEGER,
    citation                    TEXT,
    weblink                     VARCHAR(128),
    pre_release_review          VARCHAR(8),
    aggregator                  VARCHAR(32),
    count_huc12s                INTEGER,
    count_elm_ids               INTEGER
);
""")
f = fromcsv(os.path.join('wkg', args.subdir, 'Source.csv'))
f = rename(f, {
    'OBJECTID':                  'object_id',
    'Source_ID':                 'source_id',
    'Source_Name':               'source_name',
    'SourceGrp_Name':            'sourcegrp_name',
    'Use_agree':                 'use_agree',
    'Permission_request_needed': 'permission_request_needed',
    'Permission_contact_name':   'permission_contact_name',
    'Permission_contact_email':  'permission_contact_email',
    'Permission_status':         'permission_status',
    'Permission':                'permission',
    'Comment_ID':                'comment_id',
    'Citation':                  'citation',
    'Weblink':                   'weblink',
    'Pre_release_review':        'pre_release_review',
    'Aggregator':                'aggregator',
    'Count_HUC12s':              'count_huc12s',
    'Count_Elm_IDs':             'count_elm_ids'
})
todb(f, connection, 'source')

# HabitatUsage: create, map, and load
#
cursor.execute("""
DROP TABLE IF EXISTS habitat_usage;
create table habitat_usage (
    id                          BIGSERIAL NOT NULL UNIQUE PRIMARY KEY,
    object_id                   INTEGER,
    hab_usage_id                INTEGER,
    hab_usage_name              VARCHAR(32)
);
""")
f = fromcsv(os.path.join('wkg', args.subdir, 'HabitatUsage.csv'))
f = rename(f, {
    'OBJECTID':                 'object_id',
    'HabU_ID':                  'hab_usage_id',
    'HabU_Name':                'hab_usage_name',
})
todb(f, connection, 'habitat_usage')

# Element: create, map, and load
#
cursor.execute("""
DROP TABLE IF EXISTS elements;
create table elements (
    id                          BIGSERIAL NOT NULL UNIQUE PRIMARY KEY,
    object_id                   INTEGER,
    elm_scinam                  VARCHAR(64),
    elm_comnam                  VARCHAR(64),
    group_                      VARCHAR(32),
    fwa_v1                      INTEGER,
    tax_list                    VARCHAR(32),
    g_rank                      VARCHAR(16),
    s_rank                      VARCHAR(32),
    elm_scin_1                  VARCHAR(64),
    elm_scin_2                  VARCHAR(64),
    elm_scin_3                  VARCHAR(64),
    elm_scin_4                  VARCHAR(64),
    kingdom                     VARCHAR(32),
    phylum                      VARCHAR(32),
    tax_class                   VARCHAR(32),
    tax_order                   VARCHAR(32),
    family                      VARCHAR(32),
    genus                       VARCHAR(32),
    species                     VARCHAR(32),
    subsp_var                   VARCHAR(32),
    kingdom_id                  INTEGER,
    phylum_id                   INTEGER,
    tax_class_i                 INTEGER,
    tax_order_i                 INTEGER,
    family_id                   INTEGER,
    genus_id                    INTEGER,
    species_id                  INTEGER,
    elm_id                      INTEGER,
    other_id                    INTEGER,
    sensitive_fam               VARCHAR(32),
    ns_endemic                  INTEGER,
    safit_endemic               INTEGER,
    other_endemic               INTEGER,
    endemism_comment            TEXT,
    fed_list                    VARCHAR(64),
    state_list                  VARCHAR(64),
    other_list                  VARCHAR(64),
    mgtag_list                  VARCHAR(32),
    listed                      BOOLEAN,
    vulnerable                  BOOLEAN,
    endemic                     BOOLEAN,
    common                      BOOLEAN,
    not_evaluated               BOOLEAN,
    extinct                     BOOLEAN
);
""")
f = fromcsv(os.path.join('wkg', args.subdir, 'Elements.csv'))
f = rename(f, {
    'OBJECTID':               'object_id',
    'ELM_SCINAM':             'elm_scinam',
    'ELM_COMNAM':             'elm_comnam',
    'GROUP_':                 'group_',
    'FWA_v1':                 'fwa_v1',
    'TAX_LIST':               'tax_list',
    'G_Rank':                 'g_rank',
    'S_Rank':                 's_rank',
    'ELM_SCIN_1':             'elm_scin_1',
    'ELM_SCIN_2':             'elm_scin_2',
    'ELM_SCIN_3':             'elm_scin_3',
    'ELM_SCIN_4':             'elm_scin_4',
    'Kingdom':                'kingdom',
    'Phylum':                 'phylum',
    'TaxClass':               'tax_class',
    'TaxOrder':               'tax_order',
    'Family':                 'family',
    'Genus':                  'genus',
    'Species':                'species',
    'Subsp_Var':              'subsp_var',
    'Kingdom_ID':             'kingdom_id',
    'Phylum_ID':              'phylum_id',
    'TaxClass_I':             'tax_class_i',
    'TaxOrder_I':             'tax_order_i',
    'Family_ID':              'family_id',
    'Genus_ID':               'genus_id',
    'Species_ID':             'species_id',
    'ELM_ID':                 'elm_id',
    'Other_ID':               'other_id',
    'Senitive_Fam':           'sensitive_fam',
    'NS_endemic':             'ns_endemic',
    'SAFIT_endemic':          'safit_endemic',
    'Other_endemic':          'other_endemic',
    'Endemism_comment':       'endemism_comment',
    'Fed_list':               'fed_list',
    'State_list':             'state_list',
    'Other_list':             'other_list',
    'MgtAg_list':             'mgtag_list',
    'Listed':                 'listed',
    'Vulnerable':             'vulnerable',
    'Endemic':                'endemic',
    'Common':                 'common',
    'Not_evaluated':          'not_evaluated',
    'Extinct':                'extinct',
})
f = convert(f, ('fwa_v1'), lambda v: int(v))
f = convert(f, ('kingdom_id', 'phylum_id', 'tax_class_i', 'tax_order_i', 'family_id', 'genus_id', 'species_id', 'elm_id', 'other_id'), lambda v: int(float(v)))
todb(f, connection, 'elements')

# AU_v_elm: create, map, and load
#
cursor.execute("""
DROP TABLE IF EXISTS au_v_elm;
create table au_v_elm (
    id                          BIGSERIAL NOT NULL UNIQUE PRIMARY KEY,
    object_id                   INTEGER,
    huc_12                      VARCHAR(12),
    hab_usage_id                INTEGER,
    obs_typ_id                  INTEGER,
    fmt_id                      INTEGER,
    org_id                      INTEGER,
    source_id                   INTEGER,
    elm_id                      INTEGER,
    elm_type_id                 INTEGER,
    quality                     VARCHAR(16),
    amount                      DOUBLE PRECISION
);
""")
f = fromcsv(os.path.join('wkg', args.subdir, 'AU_v_elm.csv'))
f = rename(f, {
    'OBJECTID':                 'object_id',
    'HUC_12':                   'huc_12',
    'HabU_ID':                  'hab_usage_id',
    'ObsTyp_ID':                'obs_typ_id',
    'Fmt_ID':                   'fmt_id',
    'Org_ID':                   'org_id',
    'Source_ID':                'source_id',
    'Elm_ID':                   'elm_id',
    'ElmType_ID':               'elm_type_id',
    'Quality':                  'quality',
    'Amount':                   'amount',
})
f = convert(f, ('amount'), lambda v: float(v))
todb(f, connection, 'au_v_elm')


# cursor.execute("""
# UPDATE STATION SET location = ST_GeomFromText('POINT(' || -lng || ' ' || lat || ' ' || ')', 4326);
# """)

# Persist and be tidy
connection.commit()
cursor.close()
connection.close()
