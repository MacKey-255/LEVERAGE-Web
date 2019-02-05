"""Faranduleando URL Configuration"""
from django.urls import path, include
from .views import panel


urlpatterns = [
    path('', panel.as_view(), name="panel_admin"),
    path('change/', data_change.as_view(), name="panel_change_data"),
    path('rcon/', rcon.as_view(), name="panel_rcon"),
]