# Generated by Django 5.0.6 on 2024-10-07 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbase',
            name='address_line1',
        ),
        migrations.RemoveField(
            model_name='userbase',
            name='address_line2',
        ),
        migrations.RemoveField(
            model_name='userbase',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='userbase',
            name='post_code',
        ),
    ]
