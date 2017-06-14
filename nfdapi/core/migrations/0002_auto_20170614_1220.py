# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 12:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantDetails',
            fields=[
                ('taxondetails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.TaxonDetails')),
            ],
            bases=('core.taxondetails',),
        ),
        migrations.AlterField(
            model_name='occurencenaturalarea',
            name='inclusion_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='occurencetaxon',
            name='inclusion_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
