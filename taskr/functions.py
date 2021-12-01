from datetime import datetime as dt

from celery import current_app

from .models import CeleryTasks
from .tasks import add


def time_difference(date_string):
    now_time = dt.now()
    time_passed = dt.fromisoformat(date_string)
    delta = time_passed - now_time
    delta = delta.total_seconds()
    if delta < 0:
        delta = 0
    return delta


def create_celery_task(args, request, delta):
    task_id = add.apply_async(
        args=["notification", request.data], countdown=delta
    )
    if args == "create":
        a = CeleryTasks(
            task_heading=request.data.get("task_heading"),
            taskId=str(task_id),
        )
        a.save()
    elif args == "update":
        task_id = CeleryTasks.objects.get(
            task_heading=request.data.get("task_heading")
        )
        current_app.control.revoke(task_id.taskId, termination=True)
        new_task_id = add.apply_async(
            args=["notification", request.data], countdown=delta
        )
        CeleryTasks.objects.filter(
            task_heading=request.data.get("task_heading"),
        ).update(
            taskId=str(new_task_id),
        )
