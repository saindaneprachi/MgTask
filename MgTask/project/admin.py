from django.contrib import admin
from .models import Priority, Developer, Project, Task, TaskStatus

# Register your models here.
@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
    list_filter = ['first_name']
    search_fields = ['first_nam']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'developer', 'project_manager']
    list_filter = ['first_name']
    search_fields = ['first_name']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'start_date', 'end_date','is_over','assign', 'priority']
    list_filter = ['title']
    search_fields =[ 'title']

@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'project']
    list_filter = ['title']
    search_fields = ['title']