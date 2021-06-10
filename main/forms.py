from django.forms import inlineformset_factory

from .models import Car, Picture

CarImageFormset = inlineformset_factory(
    Car,
    Picture,
    fields=('img',)
)
