# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-26 17:08
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfdcore', '0031_auto_20180226_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlimeMoldLifestages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(unique=True)),
                ('name', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='slimemolddetails',
            name='lifestages',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]