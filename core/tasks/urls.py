from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskEdit, TaskDelete
from .forms import CustomTaskCreate, CustomTaskEdit


urlpatterns = [
    path('tasks/', TaskList.as_view(), name='tasks_list'),
    path('tasks/<str:pk>', TaskDetail.as_view(), name='tasks_detail'),
    path('tasks-create', TaskCreate.as_view(), name='tasks_create'),
    path('tasks-edit/<str:pk>', TaskEdit.as_view(), name='tasks_edit'),
    path('tasks-delete/<str:pk>', TaskDelete.as_view(), name='tasks_delete'),
]
