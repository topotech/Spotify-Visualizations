# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0002_auto_20160621_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='tempo',
            field=models.DecimalField(decimal_places=0, max_digits=4),
        ),
    ]
