# Generated by Django 2.1.5 on 2019-02-22 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0005_auto_20190213_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='Role'),
        ),
    ]
