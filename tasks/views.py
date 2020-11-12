from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from tasks.models import Task
from django.contrib import messages
from django.core.serializers import serialize
import json
from rest_framework.decorators import api_view

# Create your views here.


def index(request):
    return HttpResponse("Index route")


@api_view(['GET'])
def tasks(request):
    task = serialize('json', Task.objects.all())
    return HttpResponse(task, content_type="application/json")


@api_view(['POST'])
def store(request):
    try:
        payload = json.loads(request.body)
        Task.objects.create(
            title=payload["title"],
            pub_date=payload["pub_date"],
            description=payload["description"]
        )
        return HttpResponse("Task created successfully")
    except:
        raise Http404("Not found")


@api_view(['DELETE'])
def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return HttpResponse("Task deleted successfully")


@api_view(['PATCH'])
def update(request, task_id):
    try:
        payload = json.loads(request.body)
        task = Task.objects.filter(pk=task_id)
        task.update(
            title=payload["title"],
            pub_date=payload["pub_date"],
            description=payload["description"]
        )
        return HttpResponse("Task updated successfully")
    except:
        raise Http404("Not found")
