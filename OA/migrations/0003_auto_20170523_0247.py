# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 02:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OA', '0002_test'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='test',
            new_name='userinfo',
        ),
    ]
