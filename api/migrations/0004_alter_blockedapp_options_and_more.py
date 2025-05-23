# Generated by Django 4.2 on 2025-04-26 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_childdevice_nickname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blockedapp',
            options={'ordering': ['-blocked_at'], 'verbose_name': 'Blocked Application', 'verbose_name_plural': 'Blocked Applications'},
        ),
        migrations.AlterUniqueTogether(
            name='blockedapp',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='blockedapp',
            name='blocked_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blocked_apps', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blockedapp',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='blockedapp',
            name='last_synced',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blockedapp',
            name='notes',
            field=models.TextField(blank=True, help_text='Optional reason for blocking', null=True),
        ),
        migrations.AddField(
            model_name='blockedapp',
            name='package_name',
            field=models.CharField(blank=True, help_text='Android package name (e.g., com.example.app)', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blockedapp',
            name='app_name',
            field=models.CharField(help_text='User-friendly name of the application', max_length=100),
        ),
        migrations.AlterField(
            model_name='blockedapp',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocked_apps', to='api.childdevice'),
        ),
        migrations.AlterUniqueTogether(
            name='blockedapp',
            unique_together={('device', 'package_name')},
        ),
    ]
