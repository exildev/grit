# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-09 14:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epc', '0009_auto_20161009_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epc.OrdenTrabajo'),
        ),
    ]
