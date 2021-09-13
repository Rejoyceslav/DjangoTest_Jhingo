from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class CustomLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'input-dark'})
        self.fields['password'].widget.attrs.update({'class': 'input-dark'})


class CustomRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'input-dark'})
        self.fields['password1'].widget.attrs.update({'class': 'input-dark'})
        self.fields['password2'].widget.attrs.update({'class': 'input-dark'})