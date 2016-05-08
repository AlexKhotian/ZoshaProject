# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-08 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainViewHelper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textField', models.TextField()),
                ('imageField', models.FileField(blank=True, upload_to='static')),
            ],
        ),
    ]
