import json
import os

from mine.settings import MEDIA_ROOT
from system.panel.models import ResourcePack, Mods, Version
from system.lib.mcrcon import rconConnect
from system.lib.server import addWhitelistFile, removeWhitelistFile, refreshWhitelistFile
from system.utils import getUsernameToUUID, generateRandomString, is_cheat
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from system.panel.models import AntiCheat
from system.info.models import News
from system.authenticate.models import Profile, Ban
from system.lib.query.server import Query
from datetime import date


#######################################
# Enlaces Funciones para el AntiParches
#######################################


@csrf_exempt
def logout_anticheat(request):
    data = json.loads(str(request.body, encoding='utf-8'))
    try:
        user = Profile.objects.get(uuid=data.get('clientToken'))
    except Exception:
        return JsonResponse({'error': "El Usuario " + data.get('username') + " no esta registrado!"}, safe=False)

    # Comprobar IP del cliente
    if request.META.get('REMOTE_ADDR') == user.ip:
        logout(request)
        user.online = False
        user.timeActivity = now
        user.save()

        # Add file whitelist
        try:
            removeWhitelistFile(user.owner.username)
            refreshWhitelistFile()
        except Exception:
            return HttpResponse("ERROR CON EL SERVIDOR DE MINECRAFT", content_type="text/plain", status=200)

        # Reload Whitelist
        try:
            rcon = rconConnect()
            rcon.command('whitelist reload')
        except Exception:
            return JsonResponse({'error': "Error de Conexion con el Servidor Minecraft"}, safe=False)

        # Enviar Respuesta
        return JsonResponse({'request': "OK", 'error': False}, safe=False)
    else:
        return JsonResponse({'error': "Usted no esta anclado con el IP: " + request.META.get('REMOTE_ADDR')},
                            safe=False)


@csrf_exempt
def auth_anticheat(request):
    data = json.loads(str(request.body, encoding='utf-8'))
    try:
        user = Profile.objects.get(owner__username=data.get('username'))
    except Exception as e:
        return JsonResponse({'error': "El Usuario " + data.get('username') + " no esta registrado!"}, safe=False)

    # Comprobar IP del cliente
    if request.META.get('REMOTE_ADDR') == user.ip:
        auth = authenticate(username=user.owner.username, password=data.get('password'))
        # Comprobar si se logeo
        if auth is not None:
            # Logear en el Sistema & Actualizar Datos Personales
            auth.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, auth)
            user.online = True
            user.timeActivity = now
            user.save()
            # Enviar Respuesta
            data = {
                'accessToken': data.get('accessToken'),
                'selectedProfile': {
                    'id': getUsernameToUUID(user.owner.username)
                },
                'user': {
                    'id': getUsernameToUUID(user.owner.username)
                },
                'clientToken': str(user.id),
                'availableProfiles': [
                    {
                        'id': getUsernameToUUID(user.owner.username),
                        'name': user.owner.username
                    }
                ]
            }
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'error': "Contraseña Incorrecta!"}, safe=False)
    else:
        return JsonResponse({'error': "Usted no esta anclado con el IP: " + request.META.get('REMOTE_ADDR')},
                            safe=False)


@csrf_exempt
def refresh_anticheat(request):
    data = json.loads(str(request.body, encoding='utf-8'))
    try:
        user = Profile.objects.get(id=data.get('clientToken'), uuid=data.get('accessToken'))
    except Exception:
        return JsonResponse({'error': "El Usuario " + data.get('username') + " no esta registrado!"}, safe=False)

    # Comprobar IP del cliente
    if request.META.get('REMOTE_ADDR') == user.ip:
        # Logear en el Sistema & Actualizar Datos Personales
        auth = user.owner
        auth.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, auth)
        user.online = True
        user.timeActivity = now
        user.save()
        # Enviar Respuesta
        data = {
            'accessToken': data.get('accessToken'),
            'selectedProfile': {
                'id': getUsernameToUUID(user.owner.username)
            },
            'user': {
                'id': getUsernameToUUID(user.owner.username)
            },
            'clientToken': str(user.id),
            'availableProfiles': [
                {
                    'id': getUsernameToUUID(user.owner.username),
                    'name': user.owner.username
                }
            ]
        }
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': "Usted no esta anclado con el IP: " + request.META.get('REMOTE_ADDR')},
                            safe=False)


# JSON -> Whitelist remove por UUID
@csrf_exempt
def user_black(request):
    uuid = request.META.get('HTTP_ACCESS_TOKEN')
    # Buscar Usuario
    try:
        user = Profile.objects.get(uuid=uuid)
    except Exception:
        return HttpResponse("El Usuario con el ID: " + uuid + " no esta registrado!")

    # Add file whitelist
    removeWhitelistFile(user.owner.username)
    refreshWhitelistFile()
    # Reload Whitelist
    try:
        rcon = rconConnect()
        rcon.command('whitelist reload')
    except Exception:
        return HttpResponse("ERROR CONEXION CON EL SERVIDOR", content_type="text/plain", status=200)

    # Enviar Respuesta
    return HttpResponse("OK", content_type="text/plain", status=200)


# JSON -> Whitelist add por UUID
@csrf_exempt
def user_white(request):
    uuid = request.META.get('HTTP_ACCESS_TOKEN')
    # Buscar Usuario
    try:
        user = Profile.objects.get(uuid=uuid)
    except Exception:
        return HttpResponse("El Usuario con el ID: " + uuid + " no esta registrado!")

    # Add file whitelist
    try:
        addWhitelistFile(user.owner.username)
    except Exception:
        return HttpResponse("ERROR CON EL SERVIDOR DE MINECRAFT", content_type="text/plain", status=200)

    # Reload Whitelist
    try:
        rcon = rconConnect()
        rcon.command('whitelist reload')
    except Exception:
        return HttpResponse("ERROR DE CONEXION CON EL SERVIDOR", content_type="text/plain", status=200)

    # Enviar Respuesta
    return HttpResponse("OK", content_type="text/plain", status=200)


# JSON -> Ban por UUID
@csrf_exempt
def user_ban(request):
    uuid = request.META.get('HTTP_ACCESS_TOKEN')
    # Buscar Usuario
    try:
        user = Profile.objects.get(uuid=uuid)
    except Exception:
        return HttpResponse("El Usuario con el ID: " + uuid + " no esta registrado!")

    # Add Ban User
    ban = Ban(op='AntiCheat', motive='Su AntiParches ha detectado un Parche', ban_expire=0, user_ban=user.owner)
    ban.save()

    # Ban Server User
    try:
        rcon = rconConnect()
        rcon.command('ban ' + user.owner.username + ' Su AntiParches ha detectado un Parche')
    except Exception:
        return HttpResponse("ERROR CONEXION CON EL SERVIDOR", content_type="text/plain", status=200)

    # Enviar Respuesta
    return HttpResponse("OK", content_type="text/plain", status=200)


# JSON -> Upload File Crash
@csrf_exempt
def user_crash(request):
    uuid = request.META.get('HTTP_ACCESS_TOKEN')
    # Buscar Usuario
    try:
        user = Profile.objects.get(uuid=uuid)
    except Exception:
        return HttpResponse("El Usuario con el ID: " + uuid + " no esta registrado!")
    # Tomo dato del error
    data = request.body

    # Escribir Archivo de Foto
    destination = open(os.path.join(MEDIA_ROOT, 'crash/' + user.owner.username + '/' + generateRandomString() + '.log'),
                       'wb')
    destination.write(data)
    destination.close()

    return HttpResponse("OK", content_type="text/plain", status=200)


# JSON -> Upload Skin image bytes
@csrf_exempt
def user_skins(request):
    uuid = request.META.get('HTTP_ACCESS_TOKEN')
    # Buscar Usuario
    try:
        user = Profile.objects.get(uuid=uuid)
    except Exception:
        return HttpResponse("El Usuario con el ID: " + uuid + " no esta registrado!")
    # Tomo dato de la foto
    data = request.body

    # Escribir Archivo de Foto
    destination = open(os.path.join(MEDIA_ROOT, 'skins/' + user.owner.username + '.png'), 'wb')
    destination.write(data)
    destination.close()

    return HttpResponse("OK", content_type="text/plain", status=200)


# JSON -> Estado del Usuario
def user_status(request, uuid):
    # Buscar Usuario
    try:
        user = Profile.objects.get(uuid=uuid)
    except Exception:
        return JsonResponse({'error': "El Usuario con el ID: " + uuid + " no esta registrado!"}, safe=False)

    # Verificar si esta Baneado
    data = ""
    try:
        ban = Ban.objects.get(user_ban=user.owner)
        data = "BAN:" + ban.motive
    except Exception:
        # Sistema comprobador de Notificaciones
        you = Profile.objects.get(owner=request.user)
        if you.premium is not None:
            today = date.today()
            result = today.month - (you.premium.month + 1) + (0 if today.day < you.premium.day else 1)
            if result > 0:
                data = "NEWS:" + settings.ANTICHEAT_NOTIFICATION
    return HttpResponse(data, content_type="text/plain", status=200)


# JSON -> Datos del Servidor
def online(request):
    # Conectarme y Tomar Datos, en caso contrario responder que fallo
    try:
        server = Query(settings.MC_HOST, settings.MC_PORT)
        ms = server.status()
        data = {'host': settings.MC_HOST, 'port': settings.MC_PORT,
                'players': [player.name for player in ms.players.sample] if ms.players.sample is not None else [],
                'online': True, 'version': ms.version.name, 'motd': ms.description['text'],
                'numplayers': ms.players.online,
                'maxplayers': ms.players.max, 'latency': ms.latency}
    except Exception:
        data = {'host': settings.MC_HOST, 'port': settings.MC_PORT, 'online': False, 'numplayers': 0, 'maxplayers': 0}

    return JsonResponse(data, safe=False)


# JSON -> Version Actual AntiParche
def update(request):
    at = AntiCheat.objects.get(show_anticheat=True)
    if at is not None:
        data = {'version': at.version, 'url': 'http://' + request.META.get('HTTP_HOST') + at.launcher.url}
    else:
        data = {'version': False}
    return JsonResponse(data, safe=False)


# JSON -> Version Actual AntiParche
def news(request):
    news = News.objects.filter(show_anticheat=True)

    if len(news) > 0:
        data = {'entries': [{'tags': ['novedad'], 'content': {
            'en-us': {'action': 'view', 'title': obj.title, 'image': obj.image.url, 'text': obj.description}}} for obj
                            in news]}
    else:
        data = {'entries': []}
    return JsonResponse(data, safe=False)


# JSON -> Version Actual AntiParche
def friends(request):
    uuid = request.META.get('HTTP_ACCESS_TOKEN')
    # Buscar Usuario
    try:
        user = Profile.objects.get(uuid=uuid)
    except Exception:
        return HttpResponse("El Usuario con el ID: " + uuid + " no esta registrado!")

    # Devolver lista de amigos
    data = {'friends': [{'username': obj.owner.username, 'online': obj.online, 'premium': obj.premium} for obj in user]}
    return JsonResponse(data, safe=False)


# JSON -> Version Actual AntiParche
@csrf_exempt
def check_version(request):
    data = json.loads(str(request.body, encoding='utf-8'))

    try:
        version = Version.objects.get(versionId=data.get('id'))
        if version.hash == data.get('fileHash'):
            response = {'response': 'OK', 'error': False}
        else:
            response = {'response': 'Su version no concuerda con el Servidor!', 'error': True}
    except Exception:
        # Comprobar que no es algun parche
        if is_cheat(data.get('id')):
            return JsonResponse({'response': 'CHEAT', 'error': True}, safe=False)
        response = {'response': 'Su version es Invalida!', 'error': True}
    return JsonResponse(response, safe=False)


# JSON -> Version Actual AntiParche
@csrf_exempt
def check_mods(request):
    data = json.loads(str(request.body, encoding='utf-8'))
    response = {'response': 'OK', 'error': False}
    mods = Mods.objects.all()
    for obj in mods:
            for mod in data:
                if obj.name == mod.get('id') and obj.hash == mod.get('filehash'):
                    data.remove(mod)
    if len(data) > 0:
        # Comprobar que los mods sobrantes son algun parche
        for obj in data:
            if is_cheat(obj):
                return JsonResponse({'response': 'CHEAT', 'error': True}, safe=False)
        response = {'response': [{'mod': obj.get('id')} for obj in data], 'error': True}
    return JsonResponse(response, safe=False)


# JSON -> Chequea Version Minecraft (Antiparche)
@csrf_exempt
def check_resources(request):
    data = json.loads(str(request.body, encoding='utf-8'))
    response = {'response': 'OK', 'error': False}
    resources = ResourcePack.objects.all()
    for resource in resources:
            for mod in data:
                if resource.name == mod.get('id') and resource.hash == mod.get('filehash'):
                    data.remove(mod)
    if len(data) > 0:
        # Comprobar que los paquetes de recursso sobrantes son algun parche
        for obj in data:
            if is_cheat(obj):
                return JsonResponse({'response': 'CHEAT', 'error': True}, safe=False)
        response = {'response': [{'resource': obj.get('id')} for obj in data], 'error': True}
    return JsonResponse(response, safe=False)


# AJAX Servidor
def search_user(request, username):
    users = Profile.objects.filter(owner__username__contains=username)
    return JsonResponse([{'user': user.owner.username, 'online': user.online} for user in users], safe=False)


@csrf_exempt
def rcon_send(request):
    response = {'error':True, 'response': "Los datos deben ser enviados via POST"}
    if request.method == 'POST':
        if request.user.is_staff:
            try:
                rcon = rconConnect()
                rcon.command(request.POST['command'])
                response = {'error': False, 'response': "Comando enviado!"}
            except Exception:
                response = {'error': True, 'response': "Error de conexion con el Servidor"}
    return JsonResponse(response, safe=False)
