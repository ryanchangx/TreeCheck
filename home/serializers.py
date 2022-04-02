from rest_framework import serializers
from .models import *

class ProgressTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressTree
        fields = ('id', 'user_id', 'level')

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'user_id', 'task_name', 'task_description', 'task_status')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')