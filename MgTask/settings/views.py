import json
from django.http import JsonResponse
from .models import Workspace

from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(["POST","GET","PATCH","DELETE"])
def workspace(request):
    if request.method == "POST":
        params = json.loads(request.body)
        if not params.get('title'):
            return JsonResponse({
                "message": "field missing",
                "status": False,
            })
        instance = Workspace.objects.create(**params)
        return JsonResponse({
            "message" : "success",
            "status" : True,
        })

    if request.method == "GET":
        data = []
        queryset =Workspace.objects.all()
        for instance in queryset:
            data.append(instance.get_json())
        return JsonResponse({
            "message" : "success",
            "status" : True,
        })

    if request.method == "DELETE":
        data = []
        return JsonResponse({
            "message": "success",
            "status": True,
        })

    if request.method == "PATCH":
        data = []
        queryset = Workspace.objects.filter(id = 2).update(title = 'XYZ')
        return JsonResponse({
            "message" : " success",
            "status" : True,
        })




