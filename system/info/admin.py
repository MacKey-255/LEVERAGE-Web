from django.contrib import admin
from .models import News, Issues, TemplatesStatics, Donations


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)


class IssuesAdmin(admin.ModelAdmin):
    list_display = ('title',)


class TemplatesStaticsAdmin(admin.ModelAdmin):
    list_display = ('title',)


class DonationsAdmin(admin.ModelAdmin):
    list_display = ('owner',)


admin.site.register(Donations, DonationsAdmin)
admin.site.register(TemplatesStatics, TemplatesStaticsAdmin)
admin.site.register(Issues, IssuesAdmin)
admin.site.register(News, NewsAdmin)