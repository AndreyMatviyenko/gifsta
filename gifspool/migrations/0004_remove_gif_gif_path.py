# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-23 09:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifspool', '0003_auto_20170323_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gif',
            name='gif_path',
        ),
    ]