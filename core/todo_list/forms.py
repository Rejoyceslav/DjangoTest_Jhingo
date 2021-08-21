from django import forms
from django.forms import ModelForm, TextInput

from .models import *


# Widget to customize Django forms, defined in three different ways:
# 1. by adding: widget.attrs.update, in the constructor
# 2. by changing the widget in form class: field = forms.CharField(widget=forms.TextInput(attrs={}))
# 3. by setting the widget in meta class: widgets = {'field': TextInput(attrs={})}
class ToDoListForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 1.
        self.fields['title'].widget.attrs.update({
            'class': 'input-dark',
            'placeholder': 'Add new item...',
            'autofocus': 'True',
        })
    # 2. title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new item...'}))

    class Meta:
        model = ToDoList
        fields = '__all__'
        # 3.
        # widgets = {
        #     'title': TextInput(attrs={
        #         'class': 'input-dark'
        #     })
        # }
