"""Faranduleando URL Configuration"""
from django.urls import path, include
from .api import *


urlpatterns = [
	# Enlaces Funciones para el AntiParches
    #path('login/', login.as_view(), name="api_login"),
    #path('logout/', logout.as_view(), name="api_logout"),
    #path('refresh/', refresh.as_view(), name="api_refresh"),
    #path('news/', news.as_view(), name="api_news"),
    #path('notification/', notificacion.as_view(), name="api_notification"),
    #path('skins/', skins.as_view(), name="api_skins_upload"),
    #path('online/', online.as_view(), name="api_online"),
    #path('check/version/', check_version.as_view(), name="api_check_version"),
    #path('check/mods/', check_mods.as_view(), name="api_check_mods"),
    #path('check/resources/', check_resources.as_view(), name="api_check_resources"),
    ##path('client/update/', update.as_view(), name="api_update_client"),
    #path('friends/', friends.as_view(), name="api_search_friends"),
	# Enlaces Funciones para la Web
    #path('user/<username>', search.as_view(), name="api_search_user"),
    #path('rcon/', rcon.as_view(), name="api_rcon"),
    #path('server/logs/', rcon.as_view(), name="api_server_logs"),
    #path('server/start/', server_start.as_view(), name="api_server_start"),
    #path('server/stop/', server_stop.as_view(), name="api_server_stop"),
]