# Generated by Django 4.2.8 on 2024-01-06 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='hello world', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
