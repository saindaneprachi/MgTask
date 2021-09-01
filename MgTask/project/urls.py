from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [

    path('v1/project', project_view),
    path('v1/priority', priority_view),
    path('v1/task', task_view),
    path('v1/task_status', task_status_view),
]