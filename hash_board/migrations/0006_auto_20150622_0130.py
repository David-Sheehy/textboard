# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hash_board', '0005_auto_20150622_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThreadTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='name',
        ),
        migrations.AddField(
            model_name='threadtag',
            name='tag',
            field=models.ForeignKey(to='hash_board.Tag'),
        ),
        migrations.AddField(
            model_name='threadtag',
            name='thread',
            field=models.ForeignKey(to='hash_board.Thread'),
        ),
    ]
