# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-19 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0019_auto_20180219_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default=b'pic_folder/no_pic_grp.png', upload_to=b'media'),
        ),
    ]
