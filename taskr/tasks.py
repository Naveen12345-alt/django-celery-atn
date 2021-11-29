from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from celery import shared_task
from celery.utils.log import get_task_logger
from .models import Notification

# from celery.task.schedules import crontab

logger = get_task_logger(__name__)
channel_layer = get_channel_layer()


@shared_task(name="sum_two_numbers")
def add(msg, data):
    logger.info("Adding")
    # a = Notification(assignedTo = data.get('task_assigned_to'), notify_time = data.get('task_notify_time'), heading = data.get('task_heading'),description = data.get('task_description'))
    # a.save()
    async_to_sync(channel_layer.group_send)(
        "notify",
        {
            "type": "send.notification",
            "text": "notification for {}".format(data.get("task_assigned_to")),
        },
    )
    return "{}".format(msg)
