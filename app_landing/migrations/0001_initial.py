# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=b'none', max_length=50, choices=[(b'none', b'none'), (b'about', b'about'), (b'schedule', b'schedule'), (b'organizers', b'organizers'), (b'sponsors', b'sponsors'), (b'map', b'map')])),
                ('title', models.CharField(default=b'', max_length=100)),
                ('order', models.IntegerField(default=0)),
            ],
        ),
    ]
