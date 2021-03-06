from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qe_portal.settings')

#for deploy to production server:qe-port only. 
#app = Celery('qe_portal', backend='redis://qe-port:6380', broker='amqp://qe:1234@qe-port:5672')

app = Celery('qe_portal', backend='redis://localhost:6379', broker='amqp://localhost:5672')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
