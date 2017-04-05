# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-21 00:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('naivebayes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('feature', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='naivebayes.Feature')),
                ('data_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.IntegerField()),
                ('training_count', models.IntegerField()),
                ('alpha', models.IntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='feature',
            name='alpha',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='training_count',
        ),
    ]
