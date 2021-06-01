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


class CarDetailView(DetailView):
    model = Car


class ServiceList(ListView):
    model = Service


class ServiceDetailView(DetailView):
    model = Service


class PersonalItemList(ListView):
    model = PersonalItem


class PersonalItemDetailView(DetailView):
    model = PersonalItem
