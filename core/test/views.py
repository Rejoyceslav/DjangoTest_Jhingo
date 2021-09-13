from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from .forms import TestModelForm


@login_required
def test_model_form_view(request):
    my_object = Task.objects.get(id=10)
    form = TestModelForm(instance=my_object)
    context = {
        'form': form
    }
    response = render(request, 'test.html', context)
    return response
