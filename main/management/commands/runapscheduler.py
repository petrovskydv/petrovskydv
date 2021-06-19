import datetime
import logging

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django.utils.timezone import now
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from main.models import Car, Subscriber
from main.utils import send_email

logger = logging.getLogger(__name__)


def send_new_cars_email():
    new_cars_date = now() - datetime.timedelta(days=7)
    new_cars_titles = [car.title for car in Car.objects.filter(created__lte=new_cars_date)]
    recipients = [subscriber.user.email for subscriber in Subscriber.objects.all()]
    text_content = 'На сайте появилось новые объявления.'
    html_content = render_to_string('main/new_cars_email.html', new_cars_titles)
    if new_cars_titles:
        send_email(text_content, text_content, html_content, recipients)


# The `close_old_connections` decorator ensures that database connections, that have become unusable or are obsolete,
# are closed before and after our job has run.
# @util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    This job deletes APScheduler job execution entries older than `max_age` from the database. It helps to prevent the
    database from filling up with old historical records that are no longer useful.

    :param max_age: The maximum length of time to retain historical job execution records. Defaults
                    to 7 days.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            send_new_cars_email,
            trigger=CronTrigger(day_of_week="mon", hour="08", minute="00"),
            id="send_new_cars_email",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Midnight on Monday, before start of the next work week.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
