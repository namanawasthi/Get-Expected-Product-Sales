# Generated by Django 2.2.11 on 2020-06-28 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dosa', '0005_auto_20200628_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='background_image',
            field=models.ImageField(default='None', upload_to='background/'),
        ),
        migrations.AddField(
            model_name='product',
            name='youtube_link',
            field=models.TextField(default=None),
        ),
    ]
