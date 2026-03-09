from django.urls import path
from .views import delete_task, task_list, toggle_complete


urlpatterns = [
    path('', task_list, name='task_list'),
    path('delete/<int:task_id>/',delete_task, name='delete_task'),
    path('complete/<int:task_id>/',toggle_complete, name='toggle_complete'),
]

