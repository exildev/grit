# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-20 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epc', '0009_remove_actividad_completado'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='completado',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
