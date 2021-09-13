from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskEdit, TaskDelete, AddFolder, AddTagView, TagDelete, FolderDelete
from .forms import CustomTaskCreate, CustomTaskEdit


urlpatterns = [
    path('tasks/', TaskList.as_view(), name='tasks_list'),
    path('tasks/<str:pk>', TaskDetail.as_view(), name='tasks_detail'),
    path('tasks-create', TaskCreate.as_view(), name='tasks_create'),
    path('tasks-edit/<str:pk>', TaskEdit.as_view(), name='tasks_edit'),
    path('tasks-delete/<str:pk>', TaskDelete.as_view(), name='tasks_delete'),
    path('tasks-folders', AddFolder.as_view(), name='tasks_folders'),
    path('tasks-tags', AddTagView.as_view(), name='tasks_tags'),
    path('tasks-delete-tag/<str:pk>', TagDelete.as_view(), name='tasks_delete_tag'),
    path('tasks-delete-folder/<str:pk>', FolderDelete.as_view(), name='tasks_delete_folder'),
]
