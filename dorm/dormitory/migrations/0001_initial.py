# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bunk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('log_type', models.CharField(max_length=4)),
                ('datetime', models.DateTimeField()),
                ('destination', models.CharField(max_length=120, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.CharField(max_length=32)),
                ('contact_no', models.CharField(max_length=16, verbose_name=b'Contact Number')),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('mother_name', models.CharField(max_length=64)),
                ('mother_contact', models.CharField(max_length=16, verbose_name=b'Contact Number')),
                ('father_name', models.CharField(max_length=64)),
                ('father_contact', models.CharField(max_length=16, verbose_name=b'Contact Number')),
                ('guardian_name', models.CharField(max_length=64)),
                ('guardian_contact', models.CharField(max_length=16, verbose_name=b'Contact Number')),
                ('bunk', models.OneToOneField(to='dormitory.Bunk')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='log',
            name='student',
            field=models.ForeignKey(to='dormitory.Student'),
        ),
    ]
