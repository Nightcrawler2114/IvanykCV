# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0003_hobbiesandinterests_personalfeatures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobbiesandinterests',
            name='interest',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='personalfeatures',
            name='feature',
            field=models.TextField(),
        ),
    ]
