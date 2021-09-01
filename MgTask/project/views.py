from time import timezone

from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView
from .models import Project, Task, Developer, TaskStatus
import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
#API's

@require_http_methods(["POST", "GET", "PATCH", "DELETE"])
def project_view(request):
    if request.method == "POST":
        params = json.loads(request.body)
        instance = Project.objects.create(**params)
        return JsonResponse({
            "message": "success",
            "status":True,
            "data":[instance.get_json]
        })

    if request.method == "GET":
        data = []
        queryset = Project.objects.all()
        for instance in queryset:
            data.append(instance.get_json())
        return JsonResponse({
            "message" : "success",
            "status" : True,
            "data" : data
        })

    if request.method == "DELETE":
        data = []
        return JsonResponse({
            "message" : "DELETED SUCCESSFULLY",
             "status" : True,
        })

    if request.method == "PATCH":
        data = []
        queryset = Project.objects.filter()

@require_http_methods(["POST", "GET", "PATCH", "DELETE"])
def task_view(request):
    if request.method == "POST":
        params = json.loads(request.body)
        if not params.get('title'):
            return JsonResponse({
                "message" : "field missing",
                "status" : False,
            })
        instance = Task.objects.create(**params)
        return JsonResponse({
            "message": "field missing",
            "status": False,
        })
    if request.method == "GET":
        data = []
        queryset = Task.objects.all()
        for instance in queryset:
            data.append(instance.get_json())
        return JsonResponse({
            "message" : "success",
            "status" : True,
        })
    if request.method == "DELETE":
        data = []
        return JsonResponse({
            "message" : "success",
            "status" : True,
        })

    if request.method == "PATCH":
        data = []
        queryset = Task.objects.filter(title='xyz').update(assign="prachi")



@require_http_methods(["POST","GET","PATCH","DELETE"])
def task_status_view(request):
    if request.method == "POST":
        params = json.loads(request.body)
        if not params.get('title'):
            return JsonResponse({
                "message" : "field missing",
                "status" : False,
            })
        instance = Task.objects.create(**params)
        return JsonResponse({
            "message": "field missing",
            "status": False,
        })
    if request.method == "GET":
        data = []
        queryset = Task.objects.all()
        for instance in queryset:
            data.append(instance.get_json())
        return JsonResponse({
            "message" : "success",
            "status" : True,
        })
    if request.method == "DELETE":
        data = []
        return JsonResponse({
            "message" : "success",
            "status" : True,
        })

    if request.method == "PATCH":
        data = []
        queryset = Task.objects.filter(title='xyz').update(assign="prachi")


@require_http_methods(["POST", "GET", "PATCH", "DELETE"])
def developer_view(request):
    if request.method == "POST":
        params = json.loads(request.body)
        if not params.get('name'):
            return JsonResponse({
                "message": "field missing",
                "status": False,
            })
        instance = Task.objects.create(**params)
        return JsonResponse({
            "message": "field missing",
            "status": False,
        })
    if request.method == "GET":
        data = []
        queryset = Task.objects.all()
        for instance in queryset:
            data.append(instance.get_json())
        return JsonResponse({
            "message": "success",
            "status": True,
        })
    if request.method == "DELETE":
        data = []
        return JsonResponse({
            "message": "success",
            "status": True,
        })

    if request.method == "PATCH":
        data = []
        queryset = Task.objects.filter(id = 2).update(name="prachi")


@require_http_methods



