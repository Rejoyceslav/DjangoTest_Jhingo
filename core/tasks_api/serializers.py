from rest_framework import serializers
from tasks.models import Task, Tag


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'description', 'complete', 'show_task', 'folder_selected', 'create', 'tags')
