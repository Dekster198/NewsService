# Generated by Django 5.0.1 on 2024-01-23 13:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsserviceapp', '0002_alter_comment_author_alter_comment_text_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isLiked', models.BooleanField(default=False, verbose_name='Лайк')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор лайка')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsserviceapp.news', verbose_name='Новость')),
            ],
        ),
    ]
