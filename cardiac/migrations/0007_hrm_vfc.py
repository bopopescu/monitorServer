# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-15 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardiac', '0006_auto_20160129_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='hrm',
            name='vfc',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]