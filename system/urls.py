"""System URL Configuration"""
from django.urls import path
from .view import home


urlpatterns = [
	path('', home.as_view(), name='home')
    path('admin/', include('system.admin.urls')),
    path('api/', include('system.api.urls')),
    path('user/', include('system.authenticate.urls')),
    path('info/', include('system.info.urls')),
]