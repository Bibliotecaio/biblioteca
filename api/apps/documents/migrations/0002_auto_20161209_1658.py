# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['-id'], 'verbose_name': 'Документ', 'verbose_name_plural': 'Документы'},
        ),
        migrations.AlterModelOptions(
            name='documenttype',
            options={'verbose_name': 'Тип документа', 'verbose_name_plural': 'Типы документов'},
        ),
        migrations.AlterModelOptions(
            name='keyword',
            options={'verbose_name': 'Ключевое слово', 'verbose_name_plural': 'Ключеые слова'},
        ),
        migrations.AlterModelOptions(
            name='language',
            options={'verbose_name': 'Язык документа', 'verbose_name_plural': 'Языки документов'},
        ),
        migrations.AddField(
            model_name='document',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='document',
            name='document_number',
            field=models.CharField(blank=True, max_length=255, verbose_name='Название документа'),
        ),
        migrations.AddField(
            model_name='document',
            name='document_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.DocumentType', verbose_name='Тип документа'),
        ),
        migrations.AddField(
            model_name='document',
            name='file_type',
            field=models.CharField(blank=True, max_length=10, verbose_name='Тип файла'),
        ),
        migrations.AddField(
            model_name='document',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.Language', verbose_name='Язык документа'),
        ),
        migrations.AddField(
            model_name='document',
            name='page_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество страниц'),
        ),
        migrations.AddField(
            model_name='document',
            name='producer',
            field=models.CharField(blank=True, max_length=255, verbose_name='Издатель'),
        ),
        migrations.AddField(
            model_name='document',
            name='subject',
            field=models.CharField(blank=True, max_length=255, verbose_name='Тема документа'),
        ),
    ]
