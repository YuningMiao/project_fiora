# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OA', '0003_auto_20170523_0247'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='passwd',
            field=models.CharField(default=23123, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user',
            field=models.CharField(default=325324324, max_length=30),
            preserve_default=False,
        ),
    ]
