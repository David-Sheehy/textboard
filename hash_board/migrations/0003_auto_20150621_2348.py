# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hash_board', '0002_auto_20150621_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='id',
        ),
        migrations.AlterField(
            model_name='post',
            name='number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='thread',
            name='number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
