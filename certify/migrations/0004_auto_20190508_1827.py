# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-05-08 18:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certify', '0003_callbacktoken_is_invalidated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='callbacktoken',
            options={'ordering': ['-created_at']},
        ),
    ]
