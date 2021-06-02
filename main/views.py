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


class CarDetailView(DetailView):
    model = Car


class ServiceList(ListView):
    model = Service
    paginate_by = 10


class ServiceDetailView(DetailView):
    model = Service


class PersonalItemList(ListView):
    model = PersonalItem
    paginate_by = 10


class PersonalItemDetailView(DetailView):
    model = PersonalItem
