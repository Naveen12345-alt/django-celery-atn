from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .functions import create_celery_task, time_difference
from .models import Notification, Task
from .serializer import NotificationSerializer, TaskSerializer

# functions.py in all logic, no logic in views.py


class TaskCreateApi(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        delta = time_difference(request.data.get("task_notify_time")[:-1])
        print(delta)
        create_celery_task("create", request, delta)
        return self.create(request, *args, **kwargs)


class TaskListApi(generics.ListAPIView):
    permision_classes = (IsAuthenticated,)

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['task_heading',]
    # http://127.0.0.1:8000/task/api?task_heading=abcd123
    # use this url


class TaskUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def put(self, request, *args, **kwargs):
        delta = time_difference(request.data.get("task_notify_time")[:-1])
        create_celery_task("update", request, delta)
        return self.update(request, *args, **kwargs)


class TaskDeleteApi(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class NotificationListApi(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "assignedTo",
    ]
