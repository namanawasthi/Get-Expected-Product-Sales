# Generated by Django 2.2.11 on 2020-06-28 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dosa', '0004_auto_20200627_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=50),
        ),
    ]
