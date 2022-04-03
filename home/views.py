from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
# from account.api.serializer import RegistrationSerializer
from rest_framework.authtoken.models import Token

from .models import ProgressTree, Tasks, User, UserTree
from .serializers import ProgressTreeSerializer, TasksSerializer, UserSerializer, UserTreeSerializer

import random
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
        task = Tasks.objects.create(user_id=user_id, task_name=request.data['task_name'])
        task.save()
        return Response(status=201)

class DeleteTask(APIView):
    def get(self, request, task_id):
        pass

    def post(self, request, task_id):
        try:
            task = Tasks.objects.filter(task_name=request.data['task_name'])[0]
            task.delete()
            return Response(status=204)
        except Tasks.DoesNotExist:
            return Response(status=404)

class ToggleTask(APIView):
    def get(self, request, task_id):
        pass

    def post(self, request, task_id):
        try:
            task = Tasks.objects.filter(task_name=request.data['task_name'])[0]
            task.task_status = not task.task_status
            task.save()
            return Response(status=204)
        except:
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


# make user
# check user

class UserLogin(APIView):
    def get(self, request):
        try:
            query = User.objects.filter(username=request.data['username'])
            user = query[0]
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except:
            return Response(status=404)

    def post(self, request):
        query = User.objects.filter(username=request.data['username'])
        if query.count() > 0:
            user = query[0]
        else:
            user = User.objects.create(username=request.data['username'])
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UsersList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class LeaderboardData(APIView):
    def get(self, request):
        userlist = User.objects.all()
        treelist = ProgressTree.objects.all()
        for tree in treelist:
            for user in userlist:
                if tree.user_id == user.id:
                    if UserTree.objects.filter(username=user.username).count() == 0:
                        UserTree.objects.create(username=user.username, treelevel=random.randint(1, 4))
        uts = UserTreeSerializer(UserTree.objects.order_by('-treelevel'), many=True)
        return Response(uts.data)

    def post(self):
        pass


class UserProfile(APIView):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        us = UserSerializer(user)
        tasks = Tasks.objects.filter(user_id=user.id)
        ts = TasksSerializer(tasks, many=True)
        return Response({'user': us.data, 'tasks': ts.data})
    
    def post(self):
        pass