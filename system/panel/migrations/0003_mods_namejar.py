# Generated by Django 2.1.5 on 2019-02-22 09:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_anticheat_launcher'),
    ]

    operations = [
        migrations.AddField(
            model_name='mods',
            name='nameJar',
            field=models.CharField(default=django.utils.timezone.now, max_length=60, verbose_name='Nombre del Archivo'),
            preserve_default=False,
        ),
    ]
