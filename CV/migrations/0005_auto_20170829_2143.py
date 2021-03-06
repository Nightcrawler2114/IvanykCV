# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0004_auto_20170829_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.TextField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.TextField(max_length=120)),
            ],
        ),
        migrations.RenameModel(
            old_name='HobbiesAndInterests',
            new_name='HobbiesAndInterest',
        ),
        migrations.RenameModel(
            old_name='PersonalFeatures',
            new_name='PersonalFeature',
        ),
    ]
