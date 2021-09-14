from django.contrib import admin
from .models import Task, Tag, Folder, Group


admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(Folder)
admin.site.register(Group)
