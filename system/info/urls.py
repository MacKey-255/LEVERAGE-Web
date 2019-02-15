"""Faranduleando URL Configuration"""
from django.urls import path
from .views import news, webStatic, bans

urlpatterns = [
    # Vistas con Clases
    path('news/', news.as_view(), name="news"),
    path('bans/', bans.as_view(), name="bans_list"),
    path('<section>/', webStatic.as_view(), name="webStatic"),
    # path('web/<type>/', templateStatic.as_view(), name="templateStatic"),
    # Vistas con Metodo
    # path('issues/', issues.as_view(), name="issues"),
    # path('donations/', donations.as_view(), name="donations"),
]
