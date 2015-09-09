# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_landing', '0006_sponsor'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='slug',
            field=models.TextField(default=b'block'),
        ),
    ]
