from typing import Type

from django.contrib.auth.models import User
from django.db import models
from django.db.models import DateTimeField, CharField
from authentication.models import BaseClass

status = (
    (1, 'Open '),
    (2, 'Close'),

)


# create models here


class Priority(BaseClass):
    priorities = {
        (1, 'Urgent'),
        (2, 'High'),
        (3, 'Low'),
        (4, 'normal'),
    }
    title = models.CharField(max_length=50)
    priorities = models.CharField(max_length=1, choices=priorities, default='4')

    def __str__(self):
        return self.title

    def get_json(self):
        return dict(
            title = self.title,
            priorities = self.priorities,
            created = self.created,
            modified = self.modified,
        )

class Developer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(BaseClass):
    title = models.CharField(max_length=100)
    developer = models.ManyToManyField('Developer')
    project_manager = models.ForeignKey(User, on_delete=models.CASCADE)
    status =models.IntegerField(default= 1, choices=status)

    def __str__(self):
        return self.title

    def get_json(self):
        return dict(
            id=self.id,
            title=self.title,
            develoer= self.developer,
            project_manager = self.project_manager,
            created=self.created,
            modified=self.modified,
        )


class TaskStatus(models.Model):
    title = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_json(self):
        return dict(
            id=self.id,
            title=self.title,
        )


class Task(models.Model):
    title = models.CharField(max_length=50)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    assign = models.CharField(max_length= 100)
    priority = models.IntegerField(default=4, choices= Priority)
    is_over = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_json(self):
        return dict(
            id= self.id,
            title= self.title,
            start_date= self.start_date,
            end_date=self.end_date,
            assign =self.assign,
            priority=self.priority,
            is_over=self.is_over,
        )



