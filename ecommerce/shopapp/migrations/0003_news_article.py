# Generated by Django 3.2.5 on 2024-02-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_rename_user_profile_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='article',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
