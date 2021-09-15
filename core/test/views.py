from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from .forms import TestModelForm


@login_required
def test_model_form_view(request):
    if not request.user.username == "admin":
        response = render(request, 'access_denied.html')
        return response

    text = "Welcome"
    context = {
        'text': text
    }
    response = render(request, 'test.html', context)
    return response
