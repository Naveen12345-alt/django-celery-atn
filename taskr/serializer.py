from rest_framework import  serializers
from .models import Task,Notification

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        # fields = ('task_heading',)
        
        
