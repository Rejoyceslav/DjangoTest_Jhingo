from django.db import models
from django.contrib.auth.models import User


class ToDoList(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # ^ one-to-many relationship
    # ^ ForeignKey(object, on_delete=action, null=database empty field allowed, blank = submitted empty field allowed)
    title = models.CharField(max_length=10000)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  # title is now the name of item in admin
