# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hash_board', '0013_auto_20150622_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='tlp',
            field=models.TextField(default=''),
        ),
    ]
