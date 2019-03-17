import os

from django.contrib import admin
from django.core.exceptions import PermissionDenied

from mine import settings
from system.lib.mcrcon import rconConnect
from .models import Profile, Team, Ban


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('owner', 'role', 'timeActivity', 'online', 'premium', 'group', 'ip')
    list_editable = ('online', 'ip')
    actions = ('ban', 'kick', 'skins')
    raw_id_fields = ('owner',)

    def ban(self, request, queryset):
        if not request.user.is_staff:
            raise PermissionDenied
        # Tomar Usuarios a banear
        n_ban = 0
        rcon = rconConnect()
        for user in queryset:
            # Ban Server User
            try:
                rcon.command('ban-ip ' + user.ip + ' Ha sido baneado, contacte con ' + request.user.username)
                # Add Ban User
                try:
                    if Ban.objects.get(user_ban=user.owner) is None:
                        ban = Ban(op=request.user.username, motive='Ha sido baneado, contacte con ' + request.user.username,
                                  ban_expire=0, user_ban=user.owner)
                        ban.save()
                        n_ban +=1
                except Exception:
                    ban = Ban(op=request.user.username, motive='Ha sido baneado, contacte con ' + request.user.username,
                              ban_expire=0, user_ban=user.owner)
                    ban.save()
                    n_ban +=1
            except Exception as ex:
                self.message_user(request, "EL Servidor de Minecraft esta Apagado.")
                break
        self.message_user(request, "%s usuarios baneados con Exito!" % n_ban)
    ban.short_description = "Banear"

    def kick(self, request, queryset):
        if not request.user.is_staff:
            raise PermissionDenied
        # Tomar Usuarios a kickear
        n_kick = 0
        rcon = rconConnect()
        for user in queryset:
            # Ban Server User
            try:
                rcon.command('kick ' + user.owner.username + ' Ha sido kickeado por ' + request.user.username)
                n_kick+=1
            except Exception as ex:
                self.message_user(request, "EL Servidor de Minecraft esta Apagado.")
                break
        self.message_user(request, "%s usuarios kickeados con Exito!" % n_kick)
    kick.short_description = "Kickear"

    def skins(self, request, queryset):
        if not request.user.is_staff:
            raise PermissionDenied
        # Tomar Usuarios a kickear
        n = 0
        for user in queryset:
            path = settings.MEDIA_URL+'skins/' + user.owner.username + '.png'
            print(path)
            if os.path.isfile(path):
                os.remove(path)
                n+=1
        self.message_user(request, "%s skins borrados con Exito!" % n)
    skins.short_description = "Borrar Skin"


class TeamAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'description')
    raw_id_fields = ('user',)


class BanAdmin(admin.ModelAdmin):
    list_display = ('user_ban', 'ban_date', 'ban_expire', 'motive')
    actions = ('disban',)
    raw_id_fields = ('user_ban',)

    def disban(self, request, queryset):
        if not request.user.is_staff:
            raise PermissionDenied
        # Tomar Usuarios a desbanear
        n_pardon = 0
        rcon = rconConnect()
        for ban in queryset:
            # Ban Server User
            try:
                user = Profile.objects.get(owner=ban.user_ban)
                rcon.command('pardon-ip ' + user.ip)
                ban.delete()
                n_pardon +=1
            except Exception:
                self.message_user(request, "EL Servidor de Minecraft esta Apagado.")
                break
        self.message_user(request, "%s usuarios desbaneados con Exito!" % n_pardon)
    disban.short_description = "Desbanear"


admin.site.register(Ban, BanAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Profile, ProfileAdmin)