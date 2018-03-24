# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20161209_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='cover_image',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ссылка на обложку документа'),
        ),
        migrations.AddField(
            model_name='document',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания документа в системе'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='document_source_date',
            field=models.DateField(null=True, verbose_name='Дата создания оригинала документа'),
        ),
        migrations.AddField(
            model_name='document',
            name='original_document',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ссылка на оригинал документа'),
        ),
        migrations.AddField(
            model_name='document',
            name='physical_description',
            field=models.TextField(blank=True, verbose_name='Физическое описание документа'),
        ),
        migrations.AddField(
            model_name='document',
            name='preview_document',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ссылка на сконвертированную версию документа'),
        ),
        migrations.AddField(
            model_name='document',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления документа в системе'),
        ),
    ]
