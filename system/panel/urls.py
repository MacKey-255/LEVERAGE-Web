"""Minecraft URL Configuration"""
from django.urls import path
from .views import home


urlpatterns = [
    path('', home, name="panel_admin"),
    #path('change/', data_change.as_view(), name="panel_change_data"),
    #path('rcon/', rcon.as_view(), name="panel_rcon"),
    # Modificacion, Baneo & Eliminacion de usuarios
    #path('delete/<int:id>/', delete.as_view(), name="delete"),
    #path('change/<int:id>/', change.as_view(), name="change"),
    #path('skins/', skins.as_view(), name="skins"),
    #path('ban/<int:id>/', ban.as_view(), name="ban"),
    #path('pardon/<int:id>/', pardon.as_view(), name="pardon"),
]