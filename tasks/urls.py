from django.urls import path
from .views import (
    TaskCreateView, TaskListView, TaskUpdateView,
    AssignTaskView, UserTasksView, UserListCreateView
)

urlpatterns = [
    path('tasks/', TaskCreateView.as_view(), name='create-task'),
    path('tasks/all/', TaskListView.as_view(), name='all-tasks'),  # Fetch all tasks
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='update-task'),  # Update task (status, title, etc.)
    path('tasks/<int:pk>/assign/', AssignTaskView.as_view(), name='assign-task'),
    path('users/<int:user_id>/tasks/', UserTasksView.as_view(), name='user-tasks'),
    path('users/', UserListCreateView.as_view(), name='user-list'),
]
