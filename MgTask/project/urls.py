from django.urls import path
from .import views

urlpatterns = [

    path('AddProject', views.AddProject, name='AddProject'),
    path('CreateTask', views.CreateTask, name='CreateTask'),

]