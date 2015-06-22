# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hash_board', '0010_auto_20150622_0324'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ThreadTags',
            new_name='ThreadTag',
        ),
    ]
