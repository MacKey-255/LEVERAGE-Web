from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from system.validator import validate_text


# Informacion Dinamica a Mostrar
class News(models.Model):
    title = models.CharField(max_length=120, null=False, default='', verbose_name='Título')
    description = models.CharField(null=False, default='', validators=[validate_text], verbose_name='Descripcion')
    image = models.ImageField(null=False, verbose_name='Imagen Representativa')
    wroteBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wroteBy', verbose_name='Escritor')
    creationDate = models.DateField(null=False, auto_now_add=True, verbose_name='Fecha de Creacion')
	show_anticheat = models.BooleanField(null=False, default=False, verbose_name='Mostrar en el AntiParche')

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
		
    def __str__(self):
        return '%s :: %s' % (self.title, self.wroteBy.first_name, self.show_anticheat)


class TemplatesStatics(models.Model):
    title = models.CharField(max_length=240, null=False, default='', verbose_name='Título')
    content = RichTextUploadingField(null=False, default='', verbose_name='Contenido')
    type = models.BooleanField(default='enlace', null=False, verbose_name='Nombre del enlace')

    class Meta:
        verbose_name = 'Plantilla Estática'
        verbose_name_plural = 'Plantillas Estáticas'

    def __str__(self):
        return self.title


# Recopilacion de Datos
class Issues(models.Model):
    title = models.CharField(max_length=120, null=False, default='', verbose_name='Título')
    content = RichTextUploadingField(null=False, default='', verbose_name='Contenido')
    wroteBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wroteBy', verbose_name='Escritor')
    creationDate = models.DateField(null=False, auto_now_add=True, verbose_name='Fecha de Creacion')

    class Meta:
        verbose_name = 'Reporte de Error'
        verbose_name_plural = 'Reportes de Errores'

    def __str__(self):
        return self.title
		
		
class Donations(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', verbose_name='Donante')
    tarjetNauta = models.CharField(max_length=30, null=False, default='', verbose_name='Tarjeta Nauta')
    creationDate = models.DateField(null=False, auto_now_add=True, verbose_name='Fecha de la Donacion')

    class Meta:
        verbose_name = 'Donacion'
        verbose_name_plural = 'Donaciones'

    def __str__(self):
        return '%s :: %i' % (self.owner.first_name, self.tarjetNauta)

	
class Statistic(models.Model):
    date = models.DateField(null=False, auto_now_add=True, verbose_name='Fecha')
    maxJoin = models.IntegerField(null=False, default=0, verbose_name='Maximos Dentro')
	
	