from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from tasks.models import Task, Group, Folder, Tag
from .serializers import TaskSerializer


class ApiTaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pass


class ApiTaskDetail(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pass
