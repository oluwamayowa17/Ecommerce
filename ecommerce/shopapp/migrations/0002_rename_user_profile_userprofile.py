# Generated by Django 3.2.5 on 2024-02-21 10:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_profile',
            new_name='UserProfile',
        ),
    ]
