# Generated by Django 3.2.5 on 2024-02-21 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0003_news_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Category Image'),
        ),
    ]
