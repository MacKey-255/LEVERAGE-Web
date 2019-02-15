# Codigo Encargado de Leer Ficheros del Servidor
import json
import os
from mine.settings import SERVER_DIRS
from system.utils import getUsernameToUUID


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
    return {'error': "Ya usted estaba en la Lista Blanca"}


