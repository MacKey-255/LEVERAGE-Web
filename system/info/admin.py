from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.utils.timezone import now

from system.authenticate.models import Profile
from .models import News, Issues, TemplatesStatics, Donations


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'wroteBy', 'show_anticheat')
    list_editable = ('show_anticheat',)
    raw_id_fields = ('wroteBy',)


class IssuesAdmin(admin.ModelAdmin):
    list_display = ('title', 'wroteBy')
    raw_id_fields = ('wroteBy',)


class TemplatesStaticsAdmin(admin.ModelAdmin):
    list_display = ('title', 'type')


class DonationsAdmin(admin.ModelAdmin):
    list_display = ('owner', 'targetNauta', 'creationDate')
    raw_id_fields = ('owner',)
    actions = ('accept',)

    def accept(self, request, queryset):
        if not request.user.is_staff:
            raise PermissionDenied
        n = 0
        for user in queryset:
            u = Profile.objects.get(owner=user.owner)
            u.premium = now()
            u.save()
            user.delete()
            n+=1

        self.message_user(request, "%s usuarios aceptadas las Donaciones!" % n)
    accept.short_description = "Aceptar Donacion"


admin.site.register(Donations, DonationsAdmin)
admin.site.register(TemplatesStatics, TemplatesStaticsAdmin)
admin.site.register(Issues, IssuesAdmin)
admin.site.register(News, NewsAdmin)