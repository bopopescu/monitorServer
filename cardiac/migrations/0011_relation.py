# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-25 11:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cardiac', '0010_auto_20160525_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardiac.Master')),
                ('slave', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]