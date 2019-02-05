"""Faranduleando URL Configuration"""
from django.urls import path, include
from .views import templateStatic, news, issues, donations


urlpatterns = [
	# Vistas con Clases
    path('news/', news.as_view(), name="news"),
    path('web/<type>/', templateStatic.as_view(), name="templateStatic"),
	# Vistas con Metodo
    path('issues/', issues.as_view(), name="issues"),
    path('donations/', donations.as_view(), name="donations"),
]