import json

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

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
                ver = Version(vertionType=data.get('vertionType'),
                              space=data.get('diskSpace'),
                              version=data.get('version'),
                              versionId=data.get('id'))
                ver.save()
        elif request.POST['type'] == 'mods':
            mods_form = JsonForm(request.POST)
            if mods_form.is_valid():
                # Reiniciar datos
                for mods in Mods.objects.all():
                    mods.delete()
                # Guardar Datos
                for obj in data:
                    for key, values in obj.items():
                        mod = Mods(name=key,
                                   nameJar=values.get('nameJar'),
                                   space=values.get('diskSpace'),
                                   modId=values.get('id'),
                                   version=values.get('version'),
                                   vmc=values.get('vmc'))
                        mod.save()
        elif request.POST['type'] == 'resources':
            resources_form = JsonForm(request.POST)
            if resources_form.is_valid():
                # Reiniciar datos
                for resources in ResourcePack.objects.all():
                    resources.delete()
                # Guardar Datos
                for obj in data:
                    for key, values in obj.items():
                        resource = ResourcePack(name=key,
                                                space=values.get('diskSpace'))
                        resource.save()
