# Generated by Django 3.2.9 on 2021-11-30 04:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskr', '0016_auto_20211130_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celerytasks',
            name='heading',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notify_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 7, 4, 48, 37, 128854)),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_notify_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 7, 4, 48, 37, 128022)),
        ),
    ]
