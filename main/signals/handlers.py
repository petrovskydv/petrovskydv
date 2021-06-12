from django.contrib.auth.models import User, Group
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='common users'))
        send_email(instance)


def send_email(user):
    subject, from_email, to = 'hello', 'from@example.com', user.email
    text_content = 'Вы зарегистрированы на сайте.'
    html_content = '<p>Вы зарегистрированы на сайте.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
