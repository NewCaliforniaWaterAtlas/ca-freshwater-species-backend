"""
WSGI config for ca_freshwater_species_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ca_freshwater_species_backend.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Following comes from heroku doc at https://devcenter.heroku.com/articles/getting-started-with-django

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
