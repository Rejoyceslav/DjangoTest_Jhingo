from django.db import models


class ToDoList(models.Model):
    title = models.CharField(max_length=10000)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  # title is now the name of item in admin

    # def get_absolute_url(self):
    #     return