"""System URL Configuration"""
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from .view import home, Mantenimiento


urlpatterns = [
    path('', home, name='home'),
    path('admin/', include('system.panel.urls')),
    path('api/', include('system.api.urls')),
    path('user/', include('system.authenticate.urls')),
    path('info/', include('system.info.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) if not settings.MANTENIMIENTO_DEBUG else [
    path('', Mantenimiento, name='home'),
]