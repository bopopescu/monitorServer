# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardiac', '0005_health_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]