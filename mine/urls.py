"""Minecraft URL Configuration"""
from django.contrib import admin
from django.urls import path, include

from system.view import error_404, error_500


handler404 = error_404
handler500 = error_500

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('super/', admin.site.urls),
    path('', include('system.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
