# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_auto_20150312_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pathashala',
            name='Address',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
