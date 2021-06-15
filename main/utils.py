from django.core.exceptions import ValidationError
from django.utils.timezone import now


def validate_birthday(birthday):
    today = now()
    if (today.year - birthday.year) < 18:
        raise ValidationError('Вам нет 18!')