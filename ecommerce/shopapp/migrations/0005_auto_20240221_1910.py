# Generated by Django 3.2.5 on 2024-02-21 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0004_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default='02-21-2024 00:00:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='News Image'),
        ),
    ]
