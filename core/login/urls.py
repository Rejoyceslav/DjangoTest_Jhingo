from django.urls import path
from .views import MainLoginView, Register, Profile
from django.contrib.auth.views import LogoutView
from . import forms

urlpatterns = [
    path('login/', MainLoginView.as_view(authentication_form=forms.CustomLoginForm), name='login_main'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register_main'),
    path('profile/', Profile.as_view(), name='profile_main'),
]
