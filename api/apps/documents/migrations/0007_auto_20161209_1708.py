# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_document_preview_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_number',
            field=models.CharField(blank=True, max_length=255, verbose_name='Номер документа в физическом архиве'),
        ),
        migrations.AlterField(
            model_name='document',
            name='keywords',
            field=models.ManyToManyField(blank=True, null=True, to='documents.Keyword', verbose_name='Ключевые слова'),
        ),
    ]
