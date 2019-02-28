"""Minecraft URL Configuration"""
from django.urls import path
from .api import *


urlpatterns = [
    # Enlaces Funciones para el AntiParches
    path('login/', auth_anticheat, name="api_login"),
    path('logout/', logout_anticheat, name="api_logout"),
    path('refresh/', refresh_anticheat, name="api_refresh"),
    path('news/', news, name="api_news"),
    path('status/<uuid>', user_status, name="api_user_status"),
    path('black/', user_black, name="api_black"),
    path('white/', user_white, name="api_white"),
    path('ban/', user_ban, name="api_white"),
    path('skins/', user_skins, name="api_skins_upload"),
    path('online/', online, name="api_online"),
    path('check/version/', check_version, name="api_check_version"),
    path('check/mods/', check_mods, name="api_check_mods"),
    path('check/resources/', check_resources, name="api_check_resources"),
    path('client/update/', update, name="api_update_client"),
    path('friends/', friends, name="api_search_friends"),
    #  Enlaces Funciones para la Web
    path('user/<username>', search_user, name="api_search_user"),
    path('rcon/', rcon_send, name="api_rcon"),
    #path('server/logs/', server_logs, name="api_server_logs"),
    #path('server/start/', server_start, name="api_server_start"),
    #path('server/stop/', server_stop, name="api_server_stop"),
    #path('server/restart/', server_restart, name="api_server_restart"),
]