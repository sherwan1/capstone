# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-19 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0018_auto_20180218_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=10000)),
                ('creation_date', models.DateTimeField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='CourseComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='CourseFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to=b'media')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_file', to='basic_app.Course')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_uploaded_by_file', to='basic_app.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='CoursePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField()),
                ('likes', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.Course')),
                ('liked_by', models.ManyToManyField(related_name='course_liked_by', to='basic_app.Profile')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='CourseTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.Course')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='coursecomment',
            name='which_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.CoursePost'),
        ),
    ]