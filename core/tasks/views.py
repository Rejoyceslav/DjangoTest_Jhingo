from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Task
from .forms import CustomTaskCreate, CustomTaskEdit
from .filters import TaskFilter

# ListView by default look for ModelName_list.html template
# dir: app_name/templates/app_name/ModeName_list.html

# DetailView by default look for ModelName_detail.html template
# dir: app_name/templates/app_name/ModeName_detail.html

# CreateView by default look for ModelName_form.html template
# dir: app_name/templates/app_name/ModeName_form.html

# UpdateView by default look for ModelName_form.html template
# dir: app_name/templates/app_name/ModeName_form.html


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'  # since model = Task, this is equivalent to qs=Task.objects.all()
    template_name = 'tasks/task_list.html'

    def get_context_data(self, **kwargs):
        # adding data to queryset with context and filtering the data
        qs = Task.objects.all().filter(user=self.request.user)
        query = self.request.GET.get('search', None)

        if query is not None:
            qs = qs.filter(user=self.request.user).filter(title__icontains=query)

        context = super().get_context_data(**kwargs)
        context['tasks'] = qs
        # context['tasks'] = context['tasks'].filter(user=self.request.user).filter(title__icontains=query)
        # context['count'] = context['tasks'].filter(complete=False).count()
        # context['default_filter'] = default_filter
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task_detail.html'


class TaskCreate(LoginRequiredMixin, CreateView):  # uses django.forms.ModelForm
    model = Task
    form_class = CustomTaskCreate
    # fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks_list')

    def form_valid(self, form):
        # overriding this method setting user to self.request.user (currently logged in user)
        # then setting return value to default which is super(class, self).form_valid(form)
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskEdit(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = CustomTaskEdit
    # fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks_list')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks_list')
