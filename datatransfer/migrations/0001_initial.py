# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-13 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='T_DATATRANSFER_EXPDP',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_by', models.CharField(blank=True, max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=32)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('launch_user', models.CharField(help_text=b'EXPDP\xe4\xbb\xbb\xe5\x8a\xa1\xe5\x8f\x91\xe8\xb5\xb7\xe4\xba\xba', max_length=64)),
                ('db_name', models.CharField(help_text=b'db_type ip port servicename db_usage\xe7\xad\x89\xe7\x9a\x84\xe5\x88\xab\xe7\xa7\xb0 \xe7\xa1\xae\xe5\xae\x9a\xe4\xb8\x80\xe4\xb8\xaa\xe5\xae\x9e\xe4\xbe\x8b', max_length=64)),
                ('skema', models.CharField(help_text=b'\xe6\x95\xb0\xe6\x8d\xae\xe5\xba\x93schema', max_length=64)),
                ('job_name', models.CharField(db_index=True, help_text=b'EXPDP\xe4\xbb\xbb\xe5\x8a\xa1\xe5\x8f\xb7', max_length=128)),
                ('tables', models.TextField(help_text=b'\xe5\xaf\xbc\xe5\x87\xba\xe7\x9a\x84\xe8\xa1\xa8\xe6\xb8\x85\xe5\x8d\x95')),
                ('tablespace', models.TextField(help_text=b'\xe5\xaf\xbc\xe5\x87\xba\xe7\x9a\x84\xe8\xa1\xa8\xe6\xb6\x89\xe5\x8f\x8a\xe7\x9a\x84\xe8\xa1\xa8\xe7\xa9\xba\xe9\x97\xb4')),
                ('segments_bytes', models.CharField(help_text=b'\xe8\xa1\xa8\xe5\xa4\xa7\xe5\xb0\x8f\xe9\xa2\x84\xe4\xbc\xb0\xef\xbc\x8c\xe5\x8d\x95\xe4\xbd\x8d:M', max_length=32)),
                ('directory', models.CharField(help_text=b'\xe6\x95\xb0\xe6\x8d\xae\xe5\xba\x93\xe5\xaf\xbc\xe5\x87\xbadirectory', max_length=128)),
                ('dumpfilepath', models.CharField(help_text=b'\xe6\x95\xb0\xe6\x8d\xae\xe5\xba\x93\xe5\xaf\xbc\xe5\x87\xbadirectory\xe7\x9a\x84\xe8\xb7\xaf\xe5\xbe\x84', max_length=128)),
                ('expdpcommand', models.TextField(help_text=b'\xe5\xaf\xbc\xe5\x87\xba\xe5\x91\xbd\xe4\xbb\xa4')),
                ('logfile', models.TextField(help_text=b'EXPDP\xe6\x97\xa5\xe5\xbf\x97')),
                ('status', models.CharField(help_text=b'\xe5\xaf\xbc\xe5\x87\xba\xe4\xbb\xbb\xe5\x8a\xa1\xe6\x89\xa7\xe8\xa1\x8c\xe7\x8a\xb6\xe6\x80\x81', max_length=8)),
            ],
            options={
                'db_table': 'T_DATATRANSFER_EXPDP',
                'verbose_name': 'EXPDP\u4efb\u52a1\u8bb0\u5f55\u8868',
                'verbose_name_plural': 'EXPDP\u4efb\u52a1\u8bb0\u5f55\u8868',
            },
        ),
    ]