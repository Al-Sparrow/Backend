import os
from celery import Celery
from celery import shared_task
import time

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

app = Celery('NewsPaper')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'tasks': 'news.tasks.every_week_job',
        'schedule': crontab(day_of_week=1, hour=8)
    }
}

app.autodiscover_tasks()

# @shared_task
# def hello():
#     time.sleep(10)
#     print('Hello, world!')