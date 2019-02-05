"""Faranduleando URL Configuration"""
from django.urls import path, include
from .views import *


urlpatterns = [
	# Registro & Autenticacion
    path('auth/', auth.as_view(), name="auth"),
    path('register/', register.as_view(), name="register"),
    path('restore/', restore.as_view(), name="restore"),
	# Modificacion, Baneo & Eliminacion de usuarios
    path('delete/<int:id>/', delete.as_view(), name="delete"),
    path('change/<int:id>/', change.as_view(), name="change"),
    path('skins/', skins.as_view(), name="skins"),
    path('ban/<int:id>/', ban.as_view(), name="ban"),
    path('pardon/<int:id>/', pardon.as_view(), name="pardon"),
	# Ver Informacion & Online
    path('profile/<int:id>/', profile.as_view(), name="profile"),
    path('online/', online.as_view(), name="profile"),
]