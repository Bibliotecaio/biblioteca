# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-10 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0019_document_time_period'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Тема')),
            ],
            options={
                'verbose_name_plural': 'Темы документа',
                'verbose_name': 'Тема документа',
            },
        ),
        migrations.RemoveField(
            model_name='document',
            name='subject',
        ),
    ]
