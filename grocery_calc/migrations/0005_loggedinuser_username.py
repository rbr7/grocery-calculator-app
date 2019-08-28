# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtracker', '0004_loggedinuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='loggedinuser',
            name='username',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
