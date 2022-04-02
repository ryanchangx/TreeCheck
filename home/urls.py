from django.urls import path, include

from . import views

urlpatterns = [
    path('progresstrees-list', views.ProgressTreeList.as_view()),
    path('tasks-list', views.TasksList.as_view()),
]
