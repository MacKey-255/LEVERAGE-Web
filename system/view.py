from django.shortcuts import render
from django.conf import settings

from system.info.models import News


def home(request):
    return render(request, "index.html", {'news': News.objects.all().order_by('-id')[:3]})


def Mantenimiento(request):
    data = {
        'time' : settings.MANTENIMIENTO_DATE,
        'porciento': settings.MANTENIMIENTO_PORCIENTO
    }
    return render(request, 'mantenimiento/index.html', data)

def error_404(request):
    return render(request, 'error/404.html')


def error_500(request):
    return render(request, 'error/500.html')