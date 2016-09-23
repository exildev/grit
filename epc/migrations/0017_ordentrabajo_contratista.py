# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-21 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epc', '0016_auto_20160921_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordentrabajo',
            name='contratista',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='epc.Contrato'),
            preserve_default=False,
        ),
    ]
