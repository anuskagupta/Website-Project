# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2021-01-14 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehealth', '0002_remove_patient_pat_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='pat_img',
            field=models.FileField(default='static/', upload_to=b''),
            preserve_default=False,
        ),
    ]
