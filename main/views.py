from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView

from bulletin_board.settings import MAINTENANCE_MODE
from main.models import Car, Service, PersonalItem, Profile


def index(request):
    """Отображает главную страницу"""

    context = {
        'maintenance_mode': MAINTENANCE_MODE,
    }
    return render(request, 'index.html', context=context)


class CarList(ListView):
    """Отображает список объявлений с автомобилями"""

    model = Car
    paginate_by = 10

    def get_queryset(self):
        tag_filter = self.request.GET.get('tag')
        if tag_filter:
            result = Car.objects.filter(tags__id=tag_filter)
        else:
            result = super(CarList, self).get_queryset()
        return result


class CarDetailView(DetailView):
    """Отображает детальное представление объявления с автомобилем"""

    model = Car


class ServiceList(ListView):
    """Отображает список объявлений с услугами"""

    model = Service
    paginate_by = 10

    def get_queryset(self):
        tag_filter = self.request.GET.get('tag')
        if tag_filter:
            result = Service.objects.filter(tags__id=tag_filter)
        else:
            result = super(ServiceList, self).get_queryset()
        return result


class ServiceDetailView(DetailView):
    """Отображает детальное представление объявления с услугой"""

    model = Service


class PersonalItemList(ListView):
    """Отображает список объявлений с вещами"""

    model = PersonalItem
    paginate_by = 10

    def get_queryset(self):
        tag_filter = self.request.GET.get('tag')
        if tag_filter:
            result = PersonalItem.objects.filter(tags__id=tag_filter)
        else:
            result = super(PersonalItemList, self).get_queryset()
        return result


class PersonalItemDetailView(DetailView):
    """Отображает детальное представление объявления с личными вещами"""

    model = PersonalItem


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'email', 'birthdate']
