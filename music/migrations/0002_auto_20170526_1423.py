# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-26 18:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='ablum_count',
            new_name='album_count',
        ),
        migrations.RenameField(
            model_name='songs',
            old_name='song_artists',
            new_name='song_artist',
        ),
    ]
