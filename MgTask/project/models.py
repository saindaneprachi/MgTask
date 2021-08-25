from django.contrib.auth.models import User
from django.db import models

status = (
    ('1', 'Stuck'),
    ('2', 'Working'),
    ('3', 'Done'),
)

due = (
    ('1', 'On Due'),
    ('2', 'Overdue'),
    ('3', 'Done'),
)

#create models here


class AddProject(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(User, on_delete=models.CASCADE)
    assign = models.CharField(max_length=100)
    dead_line = models.DateField()
    add_date = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now_add=False, auto_now=True)
    status = models.CharField(max_length=7, choices=status, default=1)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class CreateTask(models.Model):

	project = models.CharField(max_length=100)
	assign = models.CharField(max_length=100)
	task_name = models.CharField(max_length=80)
	status = models.CharField(max_length=7, choices=status, default=1)
	due = models.CharField(max_length=7, choices=due, default=1)

	class Meta:
		ordering = ['project', 'task_name']

	def __str__(self):
		return (self.task_name)

class AddWorkspace(models.Model):
    # spacename = models.CharField(max_length=100)
    workspace = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (self.spacename)



