# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-01 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0024_document_is_document_file_processed'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='document_file_uuid',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='document',
            name='is_document_file_processed',
            field=models.BooleanField(default=False),
        ),
    ]
