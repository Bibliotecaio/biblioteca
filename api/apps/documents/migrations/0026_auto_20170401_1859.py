# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-01 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0025_auto_20170401_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_file_uuid',
            field=models.CharField(blank=True, db_index=True, max_length=255),
        ),
    ]
