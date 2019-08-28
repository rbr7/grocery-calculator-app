# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtracker', '0003_productlist_mylistown'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoggedinUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emailid', models.CharField(max_length=15)),
            ],
        ),
    ]
