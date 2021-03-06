# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 17:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pto_tier', models.FloatField(choices=[(200.0, 'Boss 5-10 Years'), (160.0, 'Boss 2-5 Years'), (120.0, 'Boss 0-2 Years'), (160.0, 'Peon 5-10 Years'), (120.0, 'Peon 2-5 Years'), (90.0, 'Peon 0-2 Years')], default=90.0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PtoHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('leave_type', models.CharField(choices=[('pto', 'PTO'), ('jury_duty', 'Jury Duty'), ('voting', 'Voting'), ('military_leave', 'Military Leave'), ('bereavement', 'Bereavement'), ('emergency', 'Emergency')], max_length=100)),
                ('is_chargeable', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
