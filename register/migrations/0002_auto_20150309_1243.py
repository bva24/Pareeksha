# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kramaha',
            name='Kramaha_Indicator',
            field=models.CharField(max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stharaha',
            name='Stharaha_Indicator',
            field=models.CharField(max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='totalquestions',
            name='Num_of_Questions',
            field=models.CharField(max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
    ]
