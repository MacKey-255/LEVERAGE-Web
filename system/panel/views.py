import json

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from mine import settings
from system.lib.mcrcon import rconConnect
from .forms import JsonForm
from .models import Version, Mods, ResourcePack, Log


# Create your views here.
@login_required(login_url='login')
def home(request):
    if not request.user.is_staff:
        return render(request, 'error/message.html', {'error': "Permisos Insuficientes para visualizar esta zona."})

    # Formularios
    version_form = JsonForm()
    version_form.fields.get('json').label = "Version (JSON)"
    version_form.fields.get('type').initial = "versions"

    mods_form = JsonForm()
    mods_form.fields.get('json').label = "Mods (JSON)"
    mods_form.fields.get('type').initial = "mods"

    resources_form = JsonForm()
    resources_form.fields.get('json').label = "ResourcesPack (JSON)"
    resources_form.fields.get('type').initial = "resources"

    data = {
        'staff': User.objects.filter(is_staff=True),
        'form_version': version_form,
        'form_mods': mods_form,
        'form_resources': resources_form
    }

    return render(request, "panel/index.html", data)


@login_required(login_url='home')
@staff_member_required()
def change(request):
    if request.method == 'POST':
        data = json.loads(str(request.POST['json']))
        # Comprobar cual formulario entro
        if request.POST['type'] == 'versions':
            version_form = JsonForm(request.POST)
            if version_form.is_valid():
                # Reiniciar datos
                for version in Version.objects.all():
                    version.delete()
                # Guardar Datos
                try:
                    ver = Version(vertionType=data.get('vertionType'),
                                  hash=data.get('fileHash'),
                                  version=data.get('version'),
                                  versionId=data.get('id'))
                    ver.save()
                except Exception:
                    print('Version no es valido')
        elif request.POST['type'] == 'mods':
            mods_form = JsonForm(request.POST)
            if mods_form.is_valid():
                # Reiniciar datos
                for mods in Mods.objects.all():
                    mods.delete()
                # Guardar Datos
                for obj in data:
                    try:
                        mod = Mods(name=obj.get('id'),
                                   hash=obj.get('filehash'))
                        mod.save()
                    except Exception:
                        print(obj + ' no es valido')
        elif request.POST['type'] == 'resources':
            resources_form = JsonForm(request.POST)
            if resources_form.is_valid():
                # Reiniciar datos
                for resources in ResourcePack.objects.all():
                    resources.delete()
                # Guardar Datos
                for obj in data:
                    try:
                        resource = ResourcePack(name=obj.get('id'),
                                                hash=obj.get('filehash'))
                        resource.save()
                    except Exception:
                        print(obj.get('id') + ' no es valido')
    return redirect('panel_admin')


@csrf_exempt
def rcon_ajax(request):
    if not request.user.is_staff:
        return JsonResponse(data={
            'error': True,
            'response': "Usuario sin Privilegios"
        }, safe=False)
    # Tomar informacion por POST
    command = request.POST['cmd']
    try:
        rcon = rconConnect()
        rcon.command(command)
        data = {
            'error': False,
            'response': "OK"
        }
    except Exception:
        data = {
            'error': True,
            'response': "Servidor Cerrado o Comando invalido!"
        }

    return JsonResponse(data, safe=False)


@csrf_exempt
def rcon(request):
    if not request.user.is_staff:
        return redirect('login')
    # Tomar informacion por POST
    command = request.POST['cmd']
    print(request.POST)
    try:
        rcon = rconConnect()
        rcon.command(command)
    except Exception:
        pass
    return redirect('panel_admin')