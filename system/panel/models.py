from django.db import models


# Create your models here.
class Version(models.Model):
    vertionType = models.CharField(max_length=20, null=False, default="RELEASE", verbose_name="Tipo de Version")
    hash = models.CharField(max_length=80, verbose_name="Hash")
    versionId = models.CharField(max_length=120, null=False, default="forge1.12.2-14.23.5.2768", verbose_name="Version de Forge")
    version = models.CharField(max_length=20, null=False, default="1.12.2", verbose_name="Version de Minecraft")

    class Meta:
        verbose_name = "Version del Juego"
        verbose_name_plural = "Versiones del Juego"

    def __str__(self):
        return self.versionId


class Mods(models.Model):
    name = models.CharField(max_length=120, verbose_name="Nombre del Archivo")
    hash = models.CharField(max_length=80, verbose_name="Hash")

    class Meta:
        verbose_name = "Mod del Juego"
        verbose_name_plural = "Mods del Juego"

    def __str__(self):
        return self.name


class ResourcePack(models.Model):
    name = models.CharField(max_length=120, verbose_name="Nombre del Archivo")
    hash = models.CharField(max_length=80, verbose_name="Hash")

    class Meta:
        verbose_name = "Paquete de Recurso"
        verbose_name_plural = "Paquetes de Recursos"

    def __str__(self):
        return self.name


class AntiCheat(models.Model):
    version = models.CharField(max_length=20, default="1.0.0", verbose_name="Version del AntiParches")
    show_anticheat = models.BooleanField(null=False, default=False, verbose_name='Mostrar en el AntiParche')
    launcher = models.FileField(null=False, verbose_name='Launcher LEVERAGE')

    class Meta:
        verbose_name = "AntiParche"
        verbose_name_plural = "AntiParches"

    def __str__(self):
        return self.version


class Log(models.Model):
    date = models.DateTimeField(auto_now=True, verbose_name='Fecha')
    action = models.CharField(max_length=300, null=False, default='Join MacKey from the Server', verbose_name='Accion')

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'

    def __str__(self):
        return '%s :: %s' % (repr(self.date), self.action)

