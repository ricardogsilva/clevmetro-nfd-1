# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170614_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='occurrencecategory',
            name='main_cat',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
