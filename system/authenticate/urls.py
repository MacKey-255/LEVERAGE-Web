"""Minecraft URL Configuration"""
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, restore, profile, online, change_ip, skins


urlpatterns = [
    # Registro & Autenticacion
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name="register"),
    path('restore/', restore, name="restore"),
    path('skins/', skins, name="upload_skins"),
    path('change_ip/<int:id>', change_ip, name="ip_config"),
    # Ver Informacion & Online
    path('profile/<int:id>/', profile, name="profile"),
    path('online/', online, name="online"),
]