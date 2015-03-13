# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_auto_20150312_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sambhavana',
            name='Sambhavana',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='special_uttama_sambhavana',
            name='Special_Prathama_Sambhavana',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='specialprathamasambhavana',
            name='Special_Prathama_Sambhavana',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
