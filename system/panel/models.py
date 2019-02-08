from django.db import models


# Create your models here.
class Version(models.Model):
    version = models.CharField(max_length=60, default="#FFF", verbose_name="Color")
	
	
class Mods(models.Model):
    version = models.CharField(max_length=60, default="#FFF", verbose_name="Color")
	

class ResourcePack(models.Model):
    version = models.CharField(max_length=60, default="#FFF", verbose_name="Color")

	
class AntiCheat(models.Model):
    version = models.CharField(max_length=20, default="1.0.0", verbose_name="Version")


class Log(models.Model):
    date = models.DateTimeField(auto_now=True, verbose_name='Fecha')
    action = models.CharField(max_length=300, null=False, default='Join MacKey from the Server', verbose_name='Accion')

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'

    def __str__(self):
        return '%s :: %i' % (repr(self.date), self.action)

