# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-18 06:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0006_auto_20191118_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follows',
            name='followee',
        ),
        migrations.RemoveField(
            model_name='follows',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='user',
        ),
        migrations.RemoveField(
            model_name='saves',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='saves',
            name='user',
        ),
        migrations.DeleteModel(
            name='Follows',
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
        migrations.DeleteModel(
            name='Saves',
        ),
    ]
