# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-14 15:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gifspool', '0003_gif_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gifview',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
