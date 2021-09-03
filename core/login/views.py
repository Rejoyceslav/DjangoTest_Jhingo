from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CustomRegisterForm, CustomLoginForm


class MainLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class Register(FormView):
    template_name = 'register.html'
    form_class = CustomRegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)


class Profile(View):

    def get(self, request):
        return render(request, 'profile_menu.html')

    def post(self, request):
        pass