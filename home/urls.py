from django.urls import path, include
from account.api.views import(registration_view)
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('progresstrees-list', views.ProgressTreeList.as_view()),
    path('tasks-list', views.TasksList.as_view()),
    path('register', registration_view, name="register"),
    path('login', obtain_auth_token, name="login"),
    path('user/<int:user_id>', views.UserRequest.as_view()),
]
