"""Faranduleando URL Configuration"""
from django.urls import path
from .views import news, webStatic, bans, issues, donations

urlpatterns = [
    path('news/', news.as_view(), name="news"),
    path('bans/', bans.as_view(), name="bans_list"),
    path('issues/', issues, name="issues"),
    path('donations/', donations, name="donations"),
    path('<section>/', webStatic.as_view(), name="webStatic"),
]
