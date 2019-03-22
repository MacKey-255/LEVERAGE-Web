"""
WSGI config for Minecraft project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os, sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(os.path.join(BASE_DIR, 'mine'))
sys.path.append(BASE_DIR)

os.environ["DJANGO_SETTINGS_MODULE"] = "mine.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()