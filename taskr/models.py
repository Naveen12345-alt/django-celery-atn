from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.
class Task(models.Model):
    task_heading = models.TextField()
    task_description = models.TextField()
    task_assigned_to = models.TextField()
    task_notify_time = models.DateTimeField(default=datetime.now() + timedelta(days=7))


class Notification(models.Model):
    assignedTo = models.TextField()
    notify_time = models.DateTimeField(default=datetime.now() + timedelta(days=7))
    heading = models.TextField(default=None)
    description = models.TextField(default=None)


# Task--->timer---> Notification(Row) ---> Id(Foreign Key)
# TaskId ---> Timer Out ---> Task id in notification
