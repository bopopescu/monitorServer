# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-25 11:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardiac', '0011_relation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='master',
            options={'ordering': ['user']},
        ),
        migrations.AlterModelOptions(
            name='relation',
            options={'ordering': ['master']},
        ),
    ]
