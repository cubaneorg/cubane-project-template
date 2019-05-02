import django
import django.core.handlers.wsgi
import os
import sys

sys.path.insert(0, '/app/')
sys.path.insert(0, '/cubane/')

os.environ['DJANGO_SETTINGS_MODULE'] = "app.settings"

django.setup()
application = django.core.handlers.wsgi.WSGIHandler()
