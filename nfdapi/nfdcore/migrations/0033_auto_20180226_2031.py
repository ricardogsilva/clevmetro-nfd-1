# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-26 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nfdcore', '0032_auto_20180226_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fungusdetails',
            name='other_observed_associations',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nfdcore.ObservedAssociations'),
        ),
    ]
