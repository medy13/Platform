# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 17:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='T_DMLAUDIT_BATCH_DETAIL',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_by', models.CharField(blank=True, max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=32)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sqlnum', models.IntegerField()),
                ('sqltext', models.TextField()),
                ('sqltype', models.CharField(choices=[(b'insert_select', b'INSERT_SELECT'), (b'insert', b'INSERT'), (b'update', b'UPDATE'), (b'delete', b'DELETE'), (b'other', b'OTHER')], max_length=16)),
                ('grammar', models.CharField(max_length=8)),
                ('gra_failreason', models.CharField(blank=True, max_length=256)),
                ('sqlplan', models.TextField(blank=True)),
                ('exetime', models.CharField(blank=True, max_length=32)),
                ('rowaffact', models.IntegerField(default=0)),
                ('audit_status', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'T_DMLAUDIT_BATCH_DETAIL',
                'verbose_name': 'DML\u6279\u6b21\u8be6\u60c5\u8868',
                'verbose_name_plural': 'DML\u6279\u6b21\u8be6\u60c5\u8868',
            },
        ),
        migrations.CreateModel(
            name='T_DMLAUDIT_BATCH_INFO',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_by', models.CharField(blank=True, max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=32)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('audit_user', models.CharField(max_length=64)),
                ('audit_batch', models.CharField(db_index=True, max_length=64)),
                ('audit_time', models.DateTimeField(auto_now_add=True)),
                ('app_name', models.CharField(max_length=64)),
                ('db_type', models.CharField(choices=[(b'oracle', b'ORACLE'), (b'mysql', b'MySQL'), (b'redis', b'REDIS')], max_length=32)),
                ('allsqltext', models.TextField()),
                ('sqlamount', models.IntegerField()),
                ('batch_status', models.CharField(blank=True, max_length=16)),
                ('evaluator', models.CharField(blank=True, max_length=64)),
                ('execute_status', models.CharField(default=b'init', max_length=8)),
                ('executor', models.CharField(blank=True, max_length=64)),
                ('exe_failreason', models.CharField(blank=True, max_length=128)),
            ],
            options={
                'db_table': 'T_DMLAUDIT_BATCH_INFO',
                'verbose_name': 'DML\u6279\u6b21\u4fe1\u606f\u8868',
                'verbose_name_plural': 'DML\u6279\u6b21\u4fe1\u606f\u8868',
            },
        ),
        migrations.AddField(
            model_name='t_dmlaudit_batch_detail',
            name='audit_batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dmlaudit.T_DMLAUDIT_BATCH_INFO'),
        ),
    ]
