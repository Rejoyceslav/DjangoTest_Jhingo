from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Task, Folder, Tag
from .forms import CustomTaskCreate, CustomTaskEdit, AddFolderForm, AddTagForm
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
        search_query = self.request.GET.get('search', None)

        if search_query is not None:
            qs = qs.filter(
                Q(user=self.request.user) &
                Q(title__icontains=search_query) |
                Q(tags__name__icontains=search_query) |
                Q(description__icontains=search_query)
                )

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


# CreateView and UpdateView both send a 'form' to appname_form.html
class TaskCreate(LoginRequiredMixin, CreateView):  # uses django.forms.ModelForm
    model = Task
    form_class = CustomTaskCreate
    # fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks_list')

    def get_form_kwargs(self):  # this creates an endpoint 'user' for, in this case, forms
        kwargs = super(TaskCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        # overriding this method setting user to self.request.user (currently logged in user)
        # then setting return value to default which is super(class, self).form_valid(form)
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


# CreateView and UpdateView both send a 'form' to appname_form.html
class TaskEdit(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = CustomTaskEdit
    # fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks_list')

    def get_form_kwargs(self):  # this creates an endpoint 'user' for, in this case, forms
        kwargs = super(TaskEdit, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks_list')


class AddFolder(View):

    def get(self, request):  # get request comes here
        items = Folder.objects.filter(user=self.request.user)
        form = AddFolderForm()

        context = {
                    'items': items,
                    'form': form,
                   }

        return render(request, 'tasks/task_add_folder.html', context)

    def post(self, request):  # post request comes here
        form = AddFolderForm(request.POST)

        if form.is_valid():
            form.instance.user = self.request.user
            form.save()

            message = f'Folder \'{form.instance.name}\' created.'
            messages.success(request, message)

            return redirect(request.path)  # redirects to request's path, <form action=''> in html has to be empty

        else:
            messages.error(request, 'Something went wrong:')
            messages.error(request, form.errors)


class AddTagView(View):

    def get(self, request):  # get request comes here
        items = Tag.objects.filter(user=self.request.user)
        form = AddTagForm()

        context = {
                    'items': items,
                    'form': form,
                   }

        return render(request, 'tasks/task_add_tag.html', context)

    def post(self, request):  # post request comes here
        form = AddTagForm(request.POST)

        if form.is_valid():
            form.instance.user = self.request.user
            form.save()

            message = f'Tag \'{form.instance.name}\' created.'
            messages.success(request, message)

            return redirect(request.path)  # redirects to request's path, <form action=''> in html has to be empty

        else:
            messages.error(request, 'Something went wrong:')
            messages.error(request, form.errors)
