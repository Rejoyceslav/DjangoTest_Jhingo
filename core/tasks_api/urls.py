from django.urls import path
from .views import ApiTaskDetail, ApiTaskList


urlpatterns = [
    path('api/tasks/', ApiTaskList.as_view(), name='tasks_api_list'),
    path('api/tasks/<int:pk>', ApiTaskDetail.as_view(), name='tasks_api_detail'),
]
