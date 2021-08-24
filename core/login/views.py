from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


class MainLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class Register(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        pass


class Profile(View):

    def get(self, request):
        return render(request, 'profile_menu.html')

    def post(self, request):
        pass