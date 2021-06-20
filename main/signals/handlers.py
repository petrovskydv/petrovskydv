from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import PersonalItem
from main.tasks import send_new_item_email_task
from main.utils import send_email


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        common_users, create = Group.objects.get_or_create(name='common users')
        instance.groups.add(common_users)
        text_content = 'Вы зарегистрированы на сайте.'
        html_content = '<p>Вы зарегистрированы на сайте.</p>'
        send_email(text_content, text_content, html_content, [instance.email])


@receiver(post_save, sender=PersonalItem)
def notify_subscribers(sender, instance, created, **kwargs):
    if created:
        send_new_item_email_task.delay(instance.id)
