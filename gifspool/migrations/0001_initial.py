# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-13 21:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gifspool.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=30)),
                ('num_gifs', models.IntegerField(default=0)),
                ('num_likes', models.IntegerField(default=0)),
                ('post_to', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('tags', models.CharField(blank=True, max_length=300)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('likes_by', models.TextField(blank=True, default='')),
                ('likes', models.IntegerField(default=0)),
                ('shocked', models.IntegerField(default=0)),
                ('loved', models.IntegerField(default=0)),
                ('laugh', models.IntegerField(default=0)),
                ('post_to', models.BooleanField(default=None)),
                ('gif_file', models.FileField(upload_to=gifspool.models.user_directory_path)),
                ('jpg_path', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('jpg_url', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('views', models.IntegerField(blank=True, default=0, null=True)),
                ('prev_gif', models.IntegerField(blank=True, default=None, null=True)),
                ('next_gif', models.IntegerField(blank=True, default=None, null=True)),
                ('creator', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GifHashtagLinker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gif', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gifspool.Gif')),
            ],
        ),
        migrations.CreateModel(
            name='GifView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=30)),
                ('view_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('gif', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gifspool.Gif')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.CharField(max_length=60, unique=True)),
                ('count', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shocked', models.BooleanField(default=False)),
                ('loved', models.BooleanField(default=False)),
                ('laugh', models.BooleanField(default=False)),
                ('like_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('gif_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gifspool.Gif')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='gifhashtaglinker',
            name='hashtag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gifspool.Hashtag'),
        ),
        migrations.AddField(
            model_name='gif',
            name='hashtags',
            field=models.ManyToManyField(blank=True, related_name='gifs_hashtag', through='gifspool.GifHashtagLinker', to='gifspool.Hashtag'),
        ),
        migrations.AddField(
            model_name='gif',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_by_user', through='gifspool.Like', to=settings.AUTH_USER_MODEL),
        ),
    ]
