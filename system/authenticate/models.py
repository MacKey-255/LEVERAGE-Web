from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


# Create your models here.
class Profile(models.Model):
    owner = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, verbose_name='Usuario')
    role = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, verbose_name="Role")
    date = models.DateField(null=False, auto_now_add=True, verbose_name='Fecha de Creacion')
    group = models.OneToOneField('Team', related_name="user_group", blank=True, verbose_name="Grupo Subscrito")
    timeActivity = models.DateTimeField(auto_now=True, verbose_name="Ultima Actividad")
    ip = models.GenericIPAddressField(null=False, verbose_name="IP")
    premium = models.DateField(null=True, default=None, verbose_name="Fecha Pago de AntiPublicidad")
    online = models.BooleanField(default=False, verbose_name="Conectado")

    def __str__(self):
        return self.owner.first_name
		
    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"

		
class Team(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_group", verbose_name="Dueño")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    name = models.CharField(max_length=50, verbose_name="Nombre del Grupo")
    description = models.CharField(max_length=150, verbose_name="Descripcion del Grupo")

    def __str__(self):
        return self.name
		
	def integrantes(self):
		return Profile.objects.filter(groups=self.id)

    class Meta:
        verbose_name = "Grupo de Amigos"
        verbose_name_plural = "Grupos de Amigos"


class Ban(models.Model):
    expulse = ((0, 'Permanente'), (60, '1 minuto'), (120, '2 minutos'))

    op = models.CharField(max_length=40, verbose_name="Operador")
    user_ban = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_ban",
                                 verbose_name="Usuario Baneado")
    motive = models.CharField(max_length=240, verbose_name="Motivo")
    ban_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Baneo")
    ban_expire = models.PositiveIntegerField(choices=expulse, verbose_name="Duracion del Ban")

    def __str__(self):
        return self.user_ban.first_name

    class Meta:
        verbose_name = "Baneado"
        verbose_name_plural = "Baneados"
