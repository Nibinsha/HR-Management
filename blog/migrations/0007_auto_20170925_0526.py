# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 05:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170925_0522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='atten',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='salar',
        ),
        migrations.AddField(
            model_name='ematt',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emsalary',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Profile'),
            preserve_default=False,
        ),
    ]
