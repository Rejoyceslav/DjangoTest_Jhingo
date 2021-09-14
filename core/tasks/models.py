from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=False)

    def __str__(self):
        return self.name


class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.name


class Group(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    title = models.CharField(max_length=70, blank=False)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    show_task = models.BooleanField(default=True)

    # relationships
    tags = models.ManyToManyField(Tag, blank=True)
    folder_selected = models.ForeignKey(Folder, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete', '-id']  # when ordering multiple values, this is the order
