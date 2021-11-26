from rest_framework import generics
from rest_framework.response import Response
from .serializer import  TaskSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import  Task

class TaskCreateApi(generics.CreateAPIView):
    permision_classes=(IsAuthenticated,)
    
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    
class TaskListApi(generics.ListAPIView):
    permision_classes=(IsAuthenticated,)

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['task_heading',]
    # http://127.0.0.1:8000/task/api?task_heading=abcd123 
    # use this url
    
class TaskUpdateApi(generics.RetrieveUpdateAPIView):
    permision_classes=(IsAuthenticated,)

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskDeleteApi(generics.DestroyAPIView):
    permision_classes=(IsAuthenticated,)

    queryset = Task.objects.all()
    serializer_class = TaskSerializer