# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Pandit_Category_Name', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Country_Name', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('District_Name', models.CharField(max_length=80, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Exam_Name', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gotra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Gotra_Name', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Guru',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Guru_Id', models.CharField(max_length=10)),
                ('Guru_Name', models.CharField(max_length=100)),
                ('Age', models.IntegerField(max_length=3, null=True, blank=True)),
                ('Guru_Address', models.TextField()),
                ('Pincode', models.IntegerField(max_length=10, null=True, blank=True)),
                ('LandLine_Num', models.IntegerField(max_length=12, null=True, blank=True)),
                ('Mobile_Num', models.IntegerField(max_length=10, null=True, blank=True)),
                ('Category', models.ForeignKey(to='register.Category')),
                ('Country', models.ForeignKey(blank=True, to='register.Country', null=True)),
                ('District', models.ForeignKey(blank=True, to='register.District', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kramaha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Kramaha_Indicator', models.IntegerField(max_length=2, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nakshatra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nakshatra_Name', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pathashala',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Pathashala_Name', models.CharField(max_length=100, null=True, blank=True)),
                ('Address', models.TextField()),
                ('Pincode', models.IntegerField(max_length=10, null=True, blank=True)),
                ('LandLine_Num', models.IntegerField(max_length=12, null=True, blank=True)),
                ('Mobile_Num', models.IntegerField(max_length=10, null=True, blank=True)),
                ('Country', models.ForeignKey(blank=True, to='register.Country', null=True)),
                ('District', models.ForeignKey(blank=True, to='register.District', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Place_Name', models.CharField(max_length=80, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sambhavana',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Sambhavana', models.IntegerField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShortExamName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Exam_Short_Name', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Special_Uttama_Sambhavana',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Special_Prathama_Sambhavana', models.IntegerField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpecialPrathamaSambhavana',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Special_Prathama_Sambhavana', models.IntegerField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('State_Name', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stharaha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Stharaha_Indicator', models.IntegerField(max_length=2, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Student_ID', models.CharField(max_length=10)),
                ('Student_Name', models.CharField(max_length=100)),
                ('Father_Name', models.CharField(max_length=100, null=True, blank=True)),
                ('Date_of_Birth', models.DateField()),
                ('Age', models.IntegerField(max_length=3, null=True, blank=True)),
                ('Permanent_Address', models.TextField()),
                ('Present_Address', models.TextField()),
                ('Pincode', models.IntegerField(max_length=10, null=True, blank=True)),
                ('LandLine_Num', models.IntegerField(max_length=12, null=True, blank=True)),
                ('Mobile_Num', models.IntegerField(max_length=10, null=True, blank=True)),
                ('Country', models.ForeignKey(blank=True, to='register.Country', null=True)),
                ('District', models.ForeignKey(blank=True, to='register.District', null=True)),
                ('Exam_Short_Name', models.ForeignKey(to='register.ShortExamName')),
                ('Guru_Details', models.ForeignKey(to='register.Guru')),
                ('Kramaha', models.ForeignKey(to='register.Kramaha')),
                ('Patashala_Name_If_Applicable', models.ForeignKey(blank=True, to='register.Pathashala', null=True)),
                ('Place', models.ForeignKey(blank=True, to='register.Place', null=True)),
                ('State', models.ForeignKey(blank=True, to='register.State', null=True)),
                ('Stharaha', models.ForeignKey(to='register.Stharaha')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sutra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Sutra_Name', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TotalQuestions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Num_of_Questions', models.IntegerField(max_length=5, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Veda_Shakha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Veda_Shakha_Name', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='student',
            name='TotalQuestions',
            field=models.ForeignKey(to='register.TotalQuestions'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='Veda_Shakha',
            field=models.ForeignKey(to='register.Veda_Shakha'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pathashala',
            name='Place',
            field=models.ForeignKey(blank=True, to='register.Place', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pathashala',
            name='State',
            field=models.ForeignKey(blank=True, to='register.State', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guru',
            name='Place',
            field=models.ForeignKey(blank=True, to='register.Place', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guru',
            name='Serving_Patashala',
            field=models.ForeignKey(blank=True, to='register.Pathashala', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guru',
            name='State',
            field=models.ForeignKey(blank=True, to='register.State', null=True),
            preserve_default=True,
        ),
    ]
