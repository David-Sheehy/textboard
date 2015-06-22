# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hash_board', '0009_auto_20150622_0242'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThreadTags',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('tag', models.ForeignKey(default=None, to='hash_board.Tag')),
                ('thread', models.ForeignKey(default=None, to='hash_board.Thread')),
            ],
        ),
        migrations.RemoveField(
            model_name='threadtag',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='threadtag',
            name='threads',
        ),
        migrations.AlterField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(to='hash_board.Thread'),
        ),
        migrations.DeleteModel(
            name='ThreadTag',
        ),
    ]
