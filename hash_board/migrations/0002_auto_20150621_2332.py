# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hash_board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='contents',
            field=models.TextField(default=''),
        ),
    ]
