# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_ptohistory_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ptohistory',
            name='title',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ptohistory',
            name='is_chargeable',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
