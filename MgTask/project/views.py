from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import ListView
from .models import AddProject, CreateTask
import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
#API's

@csrf_exempt
def addproject(request):
    if request.method == "GET":
        result = []
        addprojects = AddProject.objects.filter(title__isnull=True)
        for addproject in addprojects:
            data = {
                "id":addproject .id,     #data is variable and it is dict.type
               "name": addproject.title,
               "company": addproject.company.id,
               "assign": addproject.assign,
                "dead_line": addproject.dead_line,
                "add_date": addproject.add_date,
                 "upd_date": addproject.upd_date,
                 "status": addproject.status,
                 "description": addproject.description

            }
            result.append(data)
        return JsonResponse({'message': 'Success', 'data': result})

    if request.method == "POST":
        params = json.loads(request.body)
        isinstance = AddProject.objects.create(name=params.get('name'),
                                         company=User.objects.get(id=params.get('company')),
                                         assign=params.get('assign'),dead_line=params.get('dead_line'),
                                         add_date=params.get('add_date'),upd_date=params.get('upd_date'),
                                         status= params.get('status'), description= params.get('descrition'))
        return JsonResponse({'message': 'Success', 'data': "result"})

    if request.method == "DELETE":
        params = json.loads(request.body)
        isinstance = AddProject.objects.filter(name=params.get('name'),
                                         company=User.objects.get(id=params.get('company')),
                                         assign=params.get('assign'),dead_line=params.get('dead_line'),
                                         add_date=params.get('add_date'),upd_date=params.get('upd_date'),
                                         status= params.get('status'), description= params.get('descrition')).delete()
        return JsonResponse({'message':'Success','data': "result"})

    if request.method == "PATCH":
       params = json.loads(request.body)
       AddProject.objects.filter(add_date=params.get('author')).update(name='Tech world')
       return JsonResponse({'message': 'Success', 'data': "result"})


@csrf_exempt
def createtask(request):
    if request.method == "GET":
        result = []
        createtasks = CreateTask.objects.filter(title__isnull=True)
        for createtask in createtasks:
            data = {
                "id": createtask.id,  # data is variable and it is dict.type
                "project": createtask.project,
                "assign": createtask.assign,
                "task_name": createtask.task_name,
                "status": createtask.status,
                "due": createtask.due,
            }
            result.append(data)
        return JsonResponse({'message': 'Success', 'data': "result"})

    if request.method == "POST":
        params = json.loads(request.body)
        isinstance = CreateTask.objects.create(project=params.get('project'),
                                               assign=params.get('assign'), task_name=params.get('task_name'),
                                               status=params.get('status'), due=params.get('due'))
        return JsonResponse({'message': 'Success', 'data': "result"})

    if request.method == "DELETE":
        params = json.loads(request.body)
        isinstance = CreateTask.objects.filter(project=params.get('project'),
                                               assign=params.get('assign'), task_name=params.get('task_name'),
                                               status=params.get('status'), due=params.get('due')).delete()
        return JsonResponse({'message': 'Success', 'data': "result"})

    if request.method == "PATCH":
        params = json.loads(request.body)
        CreateTask.objects.filter(task_name=params.get('')).update(assign='prachi')
        return JsonResponse({'message': 'Success', 'data': "result"})

