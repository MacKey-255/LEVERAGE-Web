from datetime import date

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect

from system.lib.server import isWhitelistFile
from system.lib.query.server import Query
from mine import settings
from system.utils import getUsernameToUUID, OverwriteFile
from .models import Profile
from .forms import Restore, SkinsForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            profile = Profile(owner=user, uuid=getUsernameToUUID(username), ip=request.META.get('REMOTE_ADDR'), )
            profile.save()
            return redirect('home')
    else:
        form = UserCreationForm()
        form.fields.get('username').help_text = "Solo Letras y Numeros"
        form.fields.get('password1').help_text = "Solo contraseña compleja (Letras, numeros y simbolos)"
    return render(request, 'registration/register.html', {'form': form})


def restore(request):
    if request.method == 'POST':
        form = Restore(request.POST)
        if request.POST.get('password1') == request.POST.get('password2'):
            # Identificar Usuario (Buscar Usuario)
            try:
                auth = Profile.objects.get(owner__username=request.POST.get('username'),
                                           ip=request.META.get('REMOTE_ADDR'))
            except Exception:
                return render(request, 'error/message.html',
                              {'error': "Usted no posee ningun usuario anclado a su IP."})
            user = auth.owner
            user.set_password(request.POST.get('password1'))
            user.save()

            return redirect('login')
    else:
        form = Restore()
    return render(request, 'registration/restore.html', {'form': form})


@login_required(login_url='login')
def profile(request, id):
    try:
        user = Profile.objects.get(owner__id=id)
    except Exception:
        return render(request, 'error/message.html',
                      {'error': "No existe un Usuario con ese Id."})

    online = False
    try:
        server = Query(settings.MC_HOST, settings.MC_PORT)
        ms = server.status()
        for user in ms.players:
            if user == user.owner.username:
                online = True
                break
    except Exception:
        pass

    you = Profile.objects.get(owner=request.user)
    premium = True
    if you.premium is not None:
        today = date.today()
        result = today.month - (you.premium.month + 1) + (0 if today.day < you.premium.day else 1)
        if result > 0:
            premium = False
    else:
        premium = False

    data = {
        'usuario': user,
        'role': user.role.name if user.role is not None else "Usuario",
        'team': user.group.name if user.group is not None else "No es miembro de un grupo",
        'online': online,
        'whitelist': isWhitelistFile(user.owner.username),
        'premium': premium,
        'skins': SkinsForm()
    }
    return render(request, 'registration/profile.html', data)


def online(request):
    try:
        server = Query(settings.MC_HOST, settings.MC_PORT)
        ms = server.status()
        data = {'players': [player.name for player in ms.players.sample] if ms.players.sample is not None else [],
                'online': True,
                'latency': ms.latency}
    except Exception:
        data = {'online': False}
    return render(request, 'registration/online.html', data)


@login_required(login_url='login')
def change_ip(request, id):
    try:
        user = Profile.objects.get(id=id)
        if request.user.is_staff or request.user.id == id:
            user.ip = request.META.get('REMOTE_ADDR')
            user.save()
            return redirect('profile', user.id)
        else:
            return render(request, 'error/message.html',
                          {'error': "Usted no posee permisos paronlinea cambiarle el IP a " + user.owner.username})
    except Exception:
            return render(request, 'error/message.html',
                          {'error': "Este Usuario no existe!"})


@login_required(login_url='login')
def skins(request):
    if request.method == 'POST':
        form = SkinsForm(request.POST, request.FILES)
        if form.is_valid():
            fs = OverwriteFile()
            fs.save('skins/' + str(request.user.username).lower() + '.png', request.FILES['upload'])
            response = {'error': False, 'response': "OK"}
        else:
            response = {'error': True, 'response': form.errors}
    else:
        response = {'error': True, 'response': "Deben ser enviado los datos via POST!"}
    #return JsonResponse(response, safe=False)
    return redirect('profile', request.user.id)
