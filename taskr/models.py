from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.
# bydefault all field mandatory, null-True, Blank=True, helpText = 'task_explorer',
class Task(models.Model):
    task_heading = models.TextField()
    task_description = models.TextField()
    task_assigned_to = models.TextField()
    task_notify_time = models.DateTimeField(
        default=datetime.now() + timedelta(days=7)
    )

    def __str__(self):
        return self.task_heading


class Notification(models.Model):
    assignedTo = models.TextField()
    notify_time = models.DateTimeField(
        default=datetime.now() + timedelta(days=7)
    )
    heading = models.TextField(default=None)
    description = models.TextField(default=None)


class CeleryTasks(models.Model):
    task_heading = models.TextField(default=None)
    taskId = models.TextField()


# Task--->timer---> Notification(Row) ---> Id(Foreign Key)
# TaskId ---> Timer Out ---> Task id in notification
