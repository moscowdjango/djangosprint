# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_landing', '0008_auto_20150909_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
