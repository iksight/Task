from __future__ import absolute_import, unicode_literals
from os import getenv, environ
from celery import Celery
from celery.schedules import crontab

environ.setdefault("DJANGO_SETTINGS_MODULE", "Task.settings")

app = Celery('Task', backend='rpc://', broker='amqp://%s:%s@%s:%s/%s' % (
    getenv('RABBITMQ_USER',      'myuser'),
    getenv('RABBITMQ_PASSWORD',  'mypassword'),
    getenv('RABBITMQ_HOST',      '127.0.0.1'),
    getenv('RABBITMQ_PORT',      '5672'),
    getenv('RABBITMQ_VHOST',     'myvhost')
))
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'debugging_task': {
        'task': 'Task.apps.products.tasks.update_from_gsheets',
        'schedule': crontab(minute='*/1')
    },
}
