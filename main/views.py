from django.shortcuts import render
from django.views.generic import ListView, DetailView

from bulletin_board.settings import MAINTENANCE_MODE
from main.models import Car, Service, PersonalItem


def index(request):
    context = {
        'maintenance_mode': MAINTENANCE_MODE,
    }
    return render(request, 'index.html', context=context)


class CarList(ListView):
    model = Car
    paginate_by = 10

    def get_queryset(self):
        result = super(CarList, self).get_queryset()

        tag_filter = self.request.GET.get('tag')
        if tag_filter:
            result = Car.objects.filter(tags__id=tag_filter)
        return result


class CarDetailView(DetailView):
    model = Car


class ServiceList(ListView):
    model = Service
    paginate_by = 10

    def get_queryset(self):
        result = super(ServiceList, self).get_queryset()

        tag_filter = self.request.GET.get('tag')
        if tag_filter:
            result = Service.objects.filter(tags__id=tag_filter)
        return result


class ServiceDetailView(DetailView):
    model = Service


class PersonalItemList(ListView):
    model = PersonalItem
    paginate_by = 10

    def get_queryset(self):
        result = super(PersonalItemList, self).get_queryset()

        tag_filter = self.request.GET.get('tag')
        if tag_filter:
            result = PersonalItem.objects.filter(tags__id=tag_filter)
        return result


class PersonalItemDetailView(DetailView):
    model = PersonalItem
