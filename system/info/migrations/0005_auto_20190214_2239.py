# Generated by Django 2.1.5 on 2019-02-14 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_donations_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templatesstatics',
            name='type',
            field=models.CharField(default='enlace', max_length=10, verbose_name='Nombre del enlace'),
        ),
    ]