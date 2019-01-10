# ----------------------------------------------------------------------------
# Copyright (c) 2016-2019, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-05 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_helptext'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='location',
            field=models.CharField(default='Caporaso Lab, Flagstaff, AZ', max_length=300),
            preserve_default=False,
        ),
    ]
