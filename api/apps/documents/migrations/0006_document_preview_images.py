# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 17:04
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_document_toc'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='preview_images',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None), default=[], size=None),
        ),
    ]
