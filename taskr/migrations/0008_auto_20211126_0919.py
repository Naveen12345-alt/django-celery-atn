# Generated by Django 3.2.9 on 2021-11-26 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskr', '0007_auto_20211126_0918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='notification_id',
        ),
        migrations.AlterField(
            model_name='notification',
            name='notify_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 3, 9, 19, 56, 554500)),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_notify_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 3, 9, 19, 56, 554165)),
        ),
    ]
