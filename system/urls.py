"""System URL Configuration"""
from django.urls import path, include
from .view import home


urlpatterns = [
    path('', home, name='home'),
    path('admin/', include('system.panel.urls')),
    path('api/', include('system.api.urls')),
    path('user/', include('system.authenticate.urls')),
    path('info/', include('system.info.urls')),
]