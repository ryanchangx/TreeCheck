from django.urls import path, include
# from account.api.views import (registration_view)
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('progresstrees-list', views.ProgressTreeList.as_view()),
    path('userprogresstree/<int:user_id>', views.UserProgressTree.as_view()),
    path('tasks-list', views.TasksList.as_view()),
    path('usertasklist/<int:user_id>', views.UserTaskList.as_view()),
    path('addtask/<int:user_id>/<str:task_name>', views.AddTask.as_view()),
    path('deletetask/<int:task_id>', views.DeleteTask.as_view()),
    path('toggletask/<int:task_id>', views.ToggleTask.as_view()),
    # path('register', views.registration_view, name="register"),
    path('login', obtain_auth_token, name="login"),
    path('user/<int:user_id>', views.UserRequest.as_view()),
]
