from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.utils.timezone import now


def validate_birthday(birthday):
    today = now()
    if (today.year - birthday.year) < 18:
        raise ValidationError('Вам нет 18!')


def send_email(subject, text_content, html_content, recipients):
    from_email = 'from@example.com'
    msg = EmailMultiAlternatives(subject, text_content, from_email, recipients)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
