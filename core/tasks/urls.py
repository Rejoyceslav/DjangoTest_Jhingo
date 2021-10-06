from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskEdit, TaskDelete, AddFolderView, AddTagView, \
    TagDeleteView, FolderDeleteView, AddGroupView, GroupDeleteView

from .forms import CustomTaskCreate, CustomTaskEdit


urlpatterns = [
    path('tasks/', TaskList.as_view(), name='tasks_list'),
    path('tasks/<str:pk>', TaskDetail.as_view(), name='tasks_detail'),
    path('tasks-create', TaskCreate.as_view(), name='tasks_create'),
    path('tasks-edit/<str:pk>', TaskEdit.as_view(), name='tasks_edit'),
    path('tasks-delete/<str:pk>', TaskDelete.as_view(), name='tasks_delete'),

    path('tasks-folders', AddFolderView.as_view(), name='tasks_folders'),
    path('tasks-tags', AddTagView.as_view(), name='tasks_tags'),
    path('tasks-groups', AddGroupView.as_view(), name='tasks_groups'),  # disabled everywhere

    path('tasks-tag-delete/<str:pk>', TagDeleteView.as_view(), name='tasks_delete_tag'),
    path('tasks-folder-delete/<str:pk>', FolderDeleteView.as_view(), name='tasks_delete_folder'),
    path('tasks-group-delete/<str:pk>', GroupDeleteView.as_view(), name='tasks_delete_group'),
]
