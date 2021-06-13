from django.contrib.auth.models import User, Group
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import PersonalItem, Subscriber


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='common users'))
        text_content = 'Вы зарегистрированы на сайте.'
        html_content = '<p>Вы зарегистрированы на сайте.</p>'
        send_email(text_content, text_content, html_content, [instance.email])


@receiver(post_save, sender=PersonalItem)
def notify_subscribers(sender, instance, created, **kwargs):
    subscribers = Subscriber.objects.all()
    recipients = [subscriber.user.email for subscriber in subscribers]
    text_content = 'На сайте появилось новое объявление.'
    html_content = f'<p>На сайте появилось новое объявление.</p> <a href={instance.get_absolute_url()}></a>'
    send_email(text_content, text_content, html_content, recipients)


def send_email(subject, text_content, html_content, recipients):
    from_email = 'from@example.com'
    msg = EmailMultiAlternatives(subject, text_content, from_email, recipients)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
