# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-14 13:05
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0012_auto_20161212_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, verbose_name='Название документа')),
                ('document_number', models.CharField(blank=True, max_length=255, verbose_name='Номер документа в физическом архиве')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='Тема документа')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('file_type', models.CharField(blank=True, max_length=10, verbose_name='Тип файла')),
                ('producer', models.CharField(blank=True, max_length=255, verbose_name='Издатель')),
                ('page_count', models.PositiveIntegerField(default=0, verbose_name='Количество страниц')),
                ('original_document', models.CharField(blank=True, max_length=255, verbose_name='Ссылка на оригинал документа')),
                ('preview_document', models.CharField(blank=True, max_length=255, verbose_name='Ссылка на сконвертированную версию документа')),
                ('cover_image', models.CharField(blank=True, max_length=255, verbose_name='Ссылка на обложку документа')),
                ('physical_description', models.TextField(blank=True, verbose_name='Физическое описание документа')),
                ('document_source_date', models.DateField(blank=True, null=True, verbose_name='Дата создания оригинала документа')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания документа в системе')),
                ('last_update_date', models.DateTimeField(auto_now=True, verbose_name='Дата обновления документа в системе')),
                ('preview_images', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='Картинки для онлайн просмотра')),
                ('toc', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='Оглавление документа')),
                ('authors', models.ManyToManyField(blank=True, to='documents.Author', verbose_name='Авторы документа')),
                ('document_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.DocumentType', verbose_name='Тип документа')),
                ('keywords', models.ManyToManyField(blank=True, to='documents.Keyword', verbose_name='Ключевые слова')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.Language', verbose_name='Язык документа')),
            ],
            options={
                'verbose_name_plural': 'Книги',
                'verbose_name': 'Книга',
            },
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'Документ', 'verbose_name_plural': 'Документы'},
        ),
    ]
