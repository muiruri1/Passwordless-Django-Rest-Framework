# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-13 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190513_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, db_index=True, max_length=255, null=True, unique=True, verbose_name='email address'),
        ),
    ]
