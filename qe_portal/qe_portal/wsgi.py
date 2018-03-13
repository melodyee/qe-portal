"""
WSGI config for qe_portal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

''' !!! For deploy to ubuntu server  & apache2  only '''
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qe_portal.settings")
sys.path.append('/Library/WebServer/Documents/QE-PORTAL/qe_portal')
sys.path.append('/Library/WebServer/Documents/QE-PORTAL/qe_portal/qe_portal')
# sys.path.append('/var/www/qe-port/qe_portal/qe_portal')
# sys.path.append('/var/www/qe-port/qe_portal')

''' End for deploy '''

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qe_portal.settings")

application = get_wsgi_application()
