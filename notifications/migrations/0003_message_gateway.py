# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_message_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='gateway',
            field=models.CharField(default='gmail', help_text='Name of SMS /email gateway', max_length=100),
            preserve_default=False,
        ),
    ]
