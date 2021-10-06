from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.models import Task, Folder
from .forms import TestModelForm


@login_required
def test_model_form_view(request):
    if not request.user.username == "admin":  # restricts access permission to username = 'admin'
        response = render(request, 'access_denied.html')
        return response

    qs_folders = Folder.objects.all().filter(user=request.user)
    qs_folders_values = Folder.objects.all().filter(user=request.user).values()
    f = Folder.objects.get(id=5)
    all_main_tasks = f.tasks.all()
    f2 = Folder.objects.get(id=23)
    all_reallife_tasks = f2.tasks.all()

    list_of_ids = []
    for name in qs_folders_values:
        list_of_ids.append(name['id'])

    qs_tasks0 = Task.objects.all().filter(user=request.user).filter(folder_selected=list_of_ids[0])
    qs_tasks1 = Task.objects.all().filter(user=request.user).filter(folder_selected=list_of_ids[1])
    qs_tasks2 = Task.objects.all().filter(user=request.user).filter(folder_selected=list_of_ids[2])
    qs_tasks3 = Task.objects.all().filter(user=request.user).filter(folder_selected=list_of_ids[3])

    len_folders = len(qs_folders_values)
    # user_folders_dict[0]['name']
    # context.update({"color": "red"})

    context = {
        'reallife_tasks': all_reallife_tasks,
        'list_of_names': list_of_ids,
        'tasks0': qs_tasks0,
        'tasks1': qs_tasks1,
        'tasks2': qs_tasks2,
        'tasks3': qs_tasks3,
        'folders': qs_folders,
        'folders_values': qs_folders_values,
        'len_folders': len_folders,
    }
    response = render(request, 'test.html', context)
    return response


@login_required
def test_api_view(request):
    if not request.user.username == "admin":  # restricts access permission to username = 'admin'
        response = render(request, 'access_denied.html')
        return response

    context = {

    }

    response = render(request, 'test_api.html', context)
    return response
