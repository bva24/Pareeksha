# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20150309_1414'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Category_Detail',
        ),
    ]
