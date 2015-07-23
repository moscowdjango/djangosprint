# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_landing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='content',
            field=models.TextField(default=b''),
        ),
    ]
