# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-05-08 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certify', '0002_auto_20190508_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='callbacktoken',
            name='is_invalidated',
            field=models.BooleanField(default=False),
        ),
    ]
