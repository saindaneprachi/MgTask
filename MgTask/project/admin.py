from django.contrib import admin
from .models import AddProject, CreateTask, AddWorkspace

# Register your models here.
admin.site.register(AddProject)
admin.site.register(CreateTask)
admin.site.register(AddWorkspace)

