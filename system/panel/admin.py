from django.contrib import admin
from .models import *


class VersionAdmin(admin.ModelAdmin):
    list_display = ('versionId',)


class ModsAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ResourcePackAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AntiCheatAdmin(admin.ModelAdmin):
    list_display = ('version',)


admin.site.register(Version, VersionAdmin)
admin.site.register(Mods, ModsAdmin)
admin.site.register(ResourcePack, ResourcePackAdmin)
admin.site.register(AntiCheat, AntiCheatAdmin)