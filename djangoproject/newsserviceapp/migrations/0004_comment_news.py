# Generated by Django 5.0.1 on 2024-01-24 11:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsserviceapp', '0003_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='newsserviceapp.news', verbose_name='Новость'),
            preserve_default=False,
        ),
    ]
