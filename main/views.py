from django.shortcuts import render

from bulletin_board.settings import MAINTENANCE_MODE


def index(request):
    context = {
        'maintenance_mode': MAINTENANCE_MODE,
    }
    return render(request, 'index.html', context=context)
