# Codigo Encargado de Leer Ficheros del Servidor
import json
import os

from django.utils.timezone import now
from mine.settings import SERVER_DIRS
from system.utils import getUsernameToUUID, datetimeToTimestamp, timestampToDatetime
from system.authenticate.models import Profile


def addWhitelistFile(username):
    data = []
    # Lectura
    try:
        with open(os.path.join(SERVER_DIRS, 'whitelist.json')) as file:
            data = json.load(file)
    except Exception:
        pass

    # Buscar si el usuario ya existe
    for obj in data:
        if obj.get('name') == username:
            return {'error': "Ya usted estaba en la Lista Blanca"}

    # Añadir Usuario
    data.append({
        'uuid': getUsernameToUUID(username),
        'name': username,
    })

    # Escritura
    with open(os.path.join(SERVER_DIRS, 'whitelist.json'), 'w') as file:
        json.dump(data, file)


def removeWhitelistFile(username):
    data = []
    # Lectura
    try:
        with open(os.path.join(SERVER_DIRS, 'whitelist.json')) as file:
            data = json.load(file)
    except Exception:
        pass

    # Buscar si el usuario ya existe
    for obj in data:
        if obj.get('name') == username:
            # Remover Usuario
            data.remove(obj)
            # Escritura
            with open(os.path.join(SERVER_DIRS, 'whitelist.json'), 'w') as file:
                json.dump(data, file)
            break
    return {'error': "Usted no estaba en la Lista Blanca"}


def isWhitelistFile(username):
    data = []
    # Lectura
    try:
        with open(os.path.join(SERVER_DIRS, 'whitelist.json')) as file:
            data = json.load(file)
    except Exception:
        pass

    # Buscar si el usuario existe
    for obj in data:
        if obj.get('name') == username:
            return True
    return False


def refreshWhitelistFile():
    # Sacamos la fecha de ayer
    yesterday = now()
    yesterday = datetimeToTimestamp(yesterday)
    yesterday = yesterday - 3600*24  # a la hora le quitamos un dia (60*60*24)
    yesterday = timestampToDatetime(yesterday)
    # Buscamos por la fecha de ayer
    users = Profile.objects.filter(timeActivity__lte=yesterday)
    # Remover de la lista blanca a los usuarios encontrados
    for user in users:
        removeWhitelistFile(user.owner.username)