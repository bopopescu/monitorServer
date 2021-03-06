# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 12:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cardiac', '0002_auto_20160121_0802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('maxim', models.IntegerField()),
                ('minim', models.IntegerField()),
                ('average', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='hrm',
            name='commnt',
        ),
        migrations.RemoveField(
            model_name='hrm',
            name='user',
        ),
        migrations.AddField(
            model_name='hrm',
            name='comment',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hrm',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='hrm',
            name='intensity',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='hrm',
            name='state',
            field=models.CharField(max_length=10),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='health',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hrm',
            name='health',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cardiac.Health'),
            preserve_default=False,
        ),
    ]
