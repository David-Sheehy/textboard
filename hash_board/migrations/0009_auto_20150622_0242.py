# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hash_board', '0008_auto_20150622_0235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='threadtag',
            old_name='tag',
            new_name='tags',
        ),
        migrations.RenameField(
            model_name='threadtag',
            old_name='thread',
            new_name='threads',
        ),
    ]
