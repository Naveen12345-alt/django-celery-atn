from rest_framework import generics
from rest_framework.response import Response
from .serializer import NotificationSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Notification, Task
from .tasks import add


class TaskCreateApi(generics.CreateAPIView):
    # permision_classes=(IsAuthenticated,)
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        add.apply_async(args=["notification", request.data], countdown=5)
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
    permision_classes = (IsAuthenticated,)

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDeleteApi(generics.DestroyAPIView):
    permision_classes = (IsAuthenticated,)

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class NotificationListApi(generics.ListAPIView):
    # permision_classes=(IsAuthenticated,)

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
