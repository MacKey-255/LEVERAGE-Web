# Generated by Django 2.1 on 2019-02-06 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op', models.CharField(max_length=40, verbose_name='Operador')),
                ('motive', models.CharField(max_length=240, verbose_name='Motivo')),
                ('ban_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Baneo')),
                ('ban_expire', models.PositiveIntegerField(choices=[(0, 'Permanente'), (60, '1 minuto'), (120, '2 minutos')], verbose_name='Duracion del Ban')),
                ('user_ban', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ban', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Baneado')),
            ],
            options={
                'verbose_name': 'Baneado',
                'verbose_name_plural': 'Baneados',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('timeActivity', models.DateTimeField(auto_now=True, verbose_name='Ultima Actividad')),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
                ('premium', models.DateField(default=None, null=True, verbose_name='Fecha Pago de AntiPublicidad')),
                ('online', models.BooleanField(default=False, verbose_name='Conectado')),
            ],
            options={
                'verbose_name': 'Perfil de Usuario',
                'verbose_name_plural': 'Perfiles de Usuario',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre del Grupo')),
                ('description', models.CharField(max_length=150, verbose_name='Descripcion del Grupo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_group', to=settings.AUTH_USER_MODEL, verbose_name='Dueño')),
            ],
            options={
                'verbose_name': 'Grupo de Amigos',
                'verbose_name_plural': 'Grupos de Amigos',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='group',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_group', to='authenticate.Team', verbose_name='Grupo Subscrito'),
        ),
        migrations.AddField(
            model_name='profile',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='Role'),
        ),
    ]
