# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-26 12:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20160726_1218'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]
