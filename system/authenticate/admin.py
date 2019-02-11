from django.contrib import admin
from .models import Profile, Team, Ban


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('owner',)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('user',)


class BanAdmin(admin.ModelAdmin):
    list_display = ('user_ban',)


admin.site.register(Ban, BanAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Profile, ProfileAdmin)