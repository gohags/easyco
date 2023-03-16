"""
WSGI config for easyerp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.utils.regex_helper import _lazy_re_compile
import django.http.request

# from gevent import monkey

# monkey.patch_all()

django.http.request.host_validation_re = _lazy_re_compile(r"[a-zA-z0-9.:]*")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'easyerp.settings')
application = get_wsgi_application()
