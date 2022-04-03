from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
# from account.api.serializer import RegistrationSerializer
from rest_framework.authtoken.models import Token

from .models import ProgressTree, Tasks, User
from .serializers import ProgressTreeSerializer, TasksSerializer, UserSerializer

# @api_view(['POST',])
# def registration_view(request):
#     if request.method == 'POST':
#         serializer = RegistrationSerializer(data=request.data)
#         data = ()
#         if serializer.is_valid():
#             account = serializer.save()
#             data['response'] = "User created"
#             data['email'] = account.email
#             data['username'] = account.username
#             token = Token.objects.get(user=account).key
#             data['token'] = token
#         else:
#             data = serializer.errors
#         return Response(data)
    
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

class AddTask(APIView):
    def get(self, request, user_id):
        pass

    def post(self, request, user_id):
        task = Tasks.objects.create(user_id=user_id, task_name=request.data['task_name']),
        task.save()
        return Response(status=201)

class DeleteTask(APIView):
    def get(self, request, task_id):
        pass

    def post(self, request, task_id):
        try:
            task = Tasks.objects.get(task_id=task_id)
            task.delete()
            return Response(status=204)
        except Tasks.DoesNotExist:
            return Response(status=404)

class ToggleTask(APIView):
    def get(self, request, task_id):
        pass

    def post(self, request, task_id):
        try:
            task = Tasks.objects.get(task_id=task_id)
            task.task_status = not task.task_status
            task.save()
            return Response(status=204)
        except Tasks.DoesNotExist:
            return Response(status=404)

class UserTaskList(APIView):
    def get(self, request, user_id):
        tasks = Tasks.objects.filter(user_id=user_id)
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class UserProgressTree(APIView):
    def get(self, request, user_id):
        progress_trees = ProgressTree.objects.filter(user_id=user_id)
        serializer = ProgressTreeSerializer(progress_trees, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class UserRequest(APIView):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self):
        pass