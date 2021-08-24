from . import views
from django.urls import path
from .views import ToDoMain, ToDoUpdate, ToDoDelete

urlpatterns = [
    path('todo/', ToDoMain.as_view(), name='todo_main'),
    path('todo_update/<str:pk>', ToDoUpdate.as_view(), name='todo_update'),
    path('delete/<str:pk>', ToDoDelete.as_view(), name='todo_delete'),
]
