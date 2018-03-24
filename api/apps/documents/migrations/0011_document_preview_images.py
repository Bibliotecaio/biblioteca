# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 14:53
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0010_remove_document_preview_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='preview_images',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='Картинки для онлайн просмотра'),
        ),
    ]
