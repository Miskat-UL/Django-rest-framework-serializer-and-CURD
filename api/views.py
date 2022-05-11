
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Task
from .serializers import TaskSerializers


@api_view(['GET'])
def api_views(request):
    api_urls = {
        'List': '/list/'
    }


    return Response(api_urls)


@api_view(['GET'])
def task_list(request):
    task = Task.objects.all()
    serializer = TaskSerializers(task, many=True)
    return JsonResponse(serializer.data, safe=False)


    
@api_view(['GET'])
def detail_view(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializers(task, many=False)
    return Response(serializer.data)



@api_view(['POST'])
def crate_task(request):
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def update_task(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializers(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['POST'])
def delete_task(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
        
    return Response("Successfully deleted")