# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hash_board', '0006_auto_20150622_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(default=None, to='hash_board.Thread'),
        ),
        migrations.AlterField(
            model_name='threadtag',
            name='tag',
            field=models.ForeignKey(default=None, to='hash_board.Tag'),
        ),
        migrations.AlterField(
            model_name='threadtag',
            name='thread',
            field=models.ForeignKey(default=None, to='hash_board.Thread'),
        ),
    ]
