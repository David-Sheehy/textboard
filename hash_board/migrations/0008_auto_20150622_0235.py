# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hash_board', '0007_auto_20150622_0216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='threadtag',
            name='tag',
        ),
        migrations.AddField(
            model_name='threadtag',
            name='tag',
            field=models.ManyToManyField(default=None, to='hash_board.Tag'),
        ),
        migrations.RemoveField(
            model_name='threadtag',
            name='thread',
        ),
        migrations.AddField(
            model_name='threadtag',
            name='thread',
            field=models.ManyToManyField(default=None, to='hash_board.Thread'),
        ),
    ]
