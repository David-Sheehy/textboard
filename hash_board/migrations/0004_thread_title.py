# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hash_board', '0003_auto_20150621_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='title',
            field=models.TextField(max_length=42, default='default title'),
        ),
    ]
