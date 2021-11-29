from django.conf.urls import url
from django.urls import path, include
from .api import NotificationListApi, TaskCreateApi, TaskDeleteApi, TaskListApi, TaskUpdateApi

urlpatterns = [
      path('api/create',TaskCreateApi.as_view()),
      path('api/update/<int:pk>',TaskUpdateApi.as_view()),
      path('api/delete/<int:pk>',TaskDeleteApi.as_view()),
      path('api',TaskListApi.as_view()),
      path('api/notification',NotificationListApi.as_view()),
]