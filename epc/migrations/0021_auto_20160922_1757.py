# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-22 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epc', '0020_gantt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gantt',
            name='proyecto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='epc.Proyecto'),
        ),
    ]
