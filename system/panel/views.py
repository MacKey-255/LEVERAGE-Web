import json

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

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
        'resources': ResourcePack.objects.all(),
        'mods': Mods.objects.all(),
        'versions': Version.objects.all(),
        'logs': Log.objects.all().order_by('-id')[:5],
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
