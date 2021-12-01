from django.conf.urls import url
from django.urls import path, include

from .api import RegisterApi, RetrieveUserApi, UpdateUserApi
from . import views

urlpatterns = [
    path("api/register", RegisterApi.as_view()),
    path("api/update/<int:pk>", UpdateUserApi.as_view()),
    path("api/retreive", RetrieveUserApi.as_view()),
    path("api/logout", views.logout_view, name="logout_view"),
]
