# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emailid', models.CharField(max_length=30)),
                ('myList', models.TextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='newuser',
            name='emailid',
            field=models.CharField(max_length=30),
        ),
    ]
