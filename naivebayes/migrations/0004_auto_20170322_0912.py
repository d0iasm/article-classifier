# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-22 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naivebayes', '0003_auto_20170321_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='categories',
            field=models.CharField(max_length=100),
        ),
    ]
