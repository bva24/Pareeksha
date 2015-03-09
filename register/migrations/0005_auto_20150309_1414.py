# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20150309_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guru',
            old_name='Cat',
            new_name='Category',
        ),
    ]
