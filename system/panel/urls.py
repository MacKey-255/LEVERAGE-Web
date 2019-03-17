"""Minecraft URL Configuration"""
from django.urls import path
from .views import home, change, rcon

urlpatterns = [
    path('', home, name="panel_admin"),
    path('change/', change, name="panel_change_data"),
    path('rcon/', rcon, name="panel_rcon"),
]
