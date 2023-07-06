import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bulletin_board.settings')

app = Celery('bulletin_board')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_hour': {
        'task': 'announcement.tasks.mailing_list',
        'schedule': crontab(minute=0, hour='*/2'),
    },
}