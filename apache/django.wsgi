import os
import sys
path = '/www2/myblog'
if path not in sys.path:
    sys.path.insert(0, '/www2/myblog')
os.environ['DJANGO_SETTINGS_MODULE'] = 'myblog.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
