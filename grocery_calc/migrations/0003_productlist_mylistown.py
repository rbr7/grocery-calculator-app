# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtracker', '0002_auto_20170220_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlist',
            name='myListOwn',
            field=models.TextField(null=True),
        ),
    ]
