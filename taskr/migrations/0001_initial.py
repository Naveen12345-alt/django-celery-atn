# Generated by Django 3.2.9 on 2021-11-26 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField(unique=True)),
                ('task_heading', models.TextField()),
                ('task_description', models.TextField()),
                ('task_assigned_to', models.TextField()),
                ('task_notify_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_id', models.IntegerField(unique=True)),
                ('notification_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskr.task')),
            ],
        ),
    ]
