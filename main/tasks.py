import datetime

from celery import shared_task
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.timezone import now

from bulletin_board.celery import app
from main.models import Subscriber, Car
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


@app.task(name="send_new_cars_email")
def send_new_cars_email():
    new_cars_date = now() - datetime.timedelta(days=7)
    new_cars_titles = [car.title for car in Car.objects.filter(created__lte=new_cars_date)]
    recipients = [subscriber.user.email for subscriber in Subscriber.objects.all()]
    text_content = 'На сайте появилось новые объявления.'
    html_content = render_to_string('main/new_cars_email.html', new_cars_titles)
    if new_cars_titles:
        send_email(text_content, text_content, html_content, recipients)
