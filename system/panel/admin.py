from django.contrib import admin
from .models import *


class VersionAdmin(admin.ModelAdmin):
    list_display = ('versionId',)


class ModsAdmin(admin.ModelAdmin):
    list_display = ('name', 'version')


class ResourcePackAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AntiCheatAdmin(admin.ModelAdmin):
    list_display = ('version',)


class LogAdmin(admin.ModelAdmin):
    pass


admin.site.register(Version, VersionAdmin)
admin.site.register(Mods, ModsAdmin)
admin.site.register(ResourcePack, ResourcePackAdmin)
admin.site.register(AntiCheat, AntiCheatAdmin)
admin.site.register(Log, LogAdmin)