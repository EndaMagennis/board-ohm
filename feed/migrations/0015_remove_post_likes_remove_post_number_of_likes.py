# Generated by Django 4.2.8 on 2024-01-13 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0014_post_likes_delete_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='number_of_likes',
        ),
    ]