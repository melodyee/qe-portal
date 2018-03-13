from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery import Celery
from celery import task, current_task

app = Celery('tasks')
app.config_from_object('django.conf:settings')

@shared_task
def add(x, y):
    return x + y

@shared_task(queue="web")
def run_web_task(tc):
    current_task.update_state(state='PROGRESS', meta={'current': 0, 'total': 100})
    tc.run()
    current_task.update_state(state='PROGRESS', meta={'current': 100, 'total': 100})
    return tc.running

@shared_task(queue="android")
def run_android_task(tc):
    current_task.update_state(state='PROGRESS', meta={'current': 0, 'total': 100})
    tc.run()
    current_task.update_state(state='PROGRESS', meta={'current': 100, 'total': 100})
    return tc.running

@shared_task(queue="ios")
def run_ios_task(tc):
    current_task.update_state(state='PROGRESS', meta={'current': 0, 'total': 100})
    tc.run()
    current_task.update_state(state='PROGRESS', meta={'current': 100, 'total': 100})
    return tc.running
