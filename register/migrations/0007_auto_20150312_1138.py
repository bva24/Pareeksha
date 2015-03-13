# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_auto_20150310_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortexamname',
            name='Exam_Short_Name',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
