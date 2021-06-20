from celery import shared_task
from django.urls import reverse

from bulletin_board.celery import app
from main.models import Subscriber
from main.utils import send_email


@shared_task
def hello_task():
    print(f'Hello from Celery!')


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@app.task()
def send_new_item_email_task(instance_id):
    subscribers = Subscriber.objects.all()
    recipients = [subscriber.user.email for subscriber in subscribers]
    text_content = 'На сайте появилось новое объявление.'
    html_content = f'<p>На сайте появилось новое объявление.</p> ' \
                   f'<a href={reverse("items-detail", args=[instance_id])}></a>'
    send_email(text_content, text_content, html_content, recipients)
