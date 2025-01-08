# Generated by Django 5.1.4 on 2025-01-07 20:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(default='profile_pics/default.png', upload_to='profile_pics/')),
                ('city', models.CharField(blank=True, max_length=60, null=True)),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('country', models.CharField(blank=True, max_length=60, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'ordering': ['-created_at'],
            },
        ),
    ]
