# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20150309_1243'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TotalQuestions',
            new_name='TotalQuestion',
        ),
    ]
