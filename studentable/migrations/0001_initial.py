# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('mon', models.CharField(max_length=12)),
                ('tue', models.CharField(max_length=12)),
                ('wed', models.CharField(max_length=12)),
                ('thu', models.CharField(max_length=12)),
                ('fri', models.CharField(max_length=12)),
            ],
        ),
    ]
