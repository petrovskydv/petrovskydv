from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bulletin_board.settings')
app = Celery('bulletin_board')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_new_cars_email_every_monday': {
        'task': 'send_new_cars_email',
        'schedule': crontab(hour=8, minute=00, day_of_week=1),
        'args': (),
    },
}
