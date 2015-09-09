# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_landing', '0007_block_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='slug',
            field=models.CharField(default=b'block', max_length=64),
        ),
    ]
