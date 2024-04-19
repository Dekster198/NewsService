# Generated by Django 5.0.1 on 2024-04-19 07:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsserviceapp', '0005_remove_like_isliked'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('author', 'news')},
        ),
    ]