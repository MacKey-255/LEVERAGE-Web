"""Minecraft URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('super/', admin.site.urls),
    path('', include('system.urls')),
]
