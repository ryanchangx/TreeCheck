from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ProgressTree, Tasks, User
from .serializers import ProgressTreeSerializer, TasksSerializer, UserSerializer


class ProgressTreeList(APIView):
    def get(self, request):
        progress_trees = ProgressTree.objects.all()
        serializer = ProgressTreeSerializer(progress_trees, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class TasksList(APIView):
    def get(self, request):
        tasks = Tasks.objects.all()
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self):
        pass