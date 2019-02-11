from django.shortcuts import render, redirect
from django.conf import settings


def home(request):
    if request.user.is_anonymous:
        return redirect('login')

    return render(request, "index.html")


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