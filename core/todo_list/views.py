from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ToDoList
from .forms import ToDoListForm


class ToDoMain(LoginRequiredMixin, View):
    def get(self, request):  # get request comes here
        if not request.user.username == "admin":
            response = render(request, 'access_denied.html')
            return response

        items_in_list = ToDoList.objects.all()
        form = ToDoListForm()

        context = {
                    'items_in_list': items_in_list,
                    'form': form,
                   }

        return render(request, 'todo_main.html', context)

    def post(self, request):  # post request comes here
        form = ToDoListForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect(request.path)  # redirects to request's path, <form action=''> in html has to be empty


class ToDoUpdate(LoginRequiredMixin, View):
    def get(self, request, pk):  # get request comes here, pk = primary key
        item = ToDoList.objects.get(id=pk)
        form = ToDoListForm(instance=item)

        context = {'form': form}

        return render(request, 'todo_update.html', context)

    def post(self, request, pk):  # post request comes here
        item = ToDoList.objects.get(id=pk)
        form = ToDoListForm(request.POST, instance=item)
        if form.is_valid():
            form.save()

        return redirect('todo_main')  # 'todo_main' is url name from urls


class ToDoDelete(LoginRequiredMixin, View):
    def get(self, request, pk):  # get request comes here, pk = primary key
        # item = ToDoList.objects.get(id=pk)
        item = get_object_or_404(ToDoList, id=pk)  # if object is not found, show 404
        context = {'item': item}
        return render(request, 'todo_delete.html', context)

    def post(self, request, pk):  # post request comes here
        item = ToDoList.objects.get(id=pk)
        item.delete()

        return redirect('todo_main')  # 'to_do_main' is url name from urls

