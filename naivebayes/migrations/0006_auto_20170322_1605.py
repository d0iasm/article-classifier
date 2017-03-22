# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-22 07:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('naivebayes', '0005_auto_20170322_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('count', models.IntegerField(default=0)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naivebayes.Feature')),
            ],
        ),
        migrations.RemoveField(
            model_name='categorycount',
            name='category',
        ),
        migrations.RemoveField(
            model_name='featurecount',
            name='feature',
        ),
        migrations.AddField(
            model_name='category',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='CategoryCount',
        ),
        migrations.DeleteModel(
            name='FeatureCount',
        ),
    ]