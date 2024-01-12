# Generated by Django 4.2.8 on 2024-01-12 00:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0010_alter_post_age_range_alter_post_number_of_players'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='like',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
    ]