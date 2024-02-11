from django.urls import path
from .views import task_lists, add_task, delete_task, update_task

urlpatterns = [
    path('list/', task_lists, name='task_lists'),
    path('add/', add_task, name='add_task'),
    path('delete/<int:todo_id>/', delete_task, name='delete_task'),
    path('update/<int:todo_id>/', update_task, name='update_task'),
]
