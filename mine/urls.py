"""Minecraft URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('super/', admin.site.urls),
    path('', include('system.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
