from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from account.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token

from .models import ProgressTree, Tasks, User
from .serializers import ProgressTreeSerializer, TasksSerializer, UserSerializer

@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = ()
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "User created"
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
    
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