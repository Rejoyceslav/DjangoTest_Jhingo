from django.views.generic.edit import CreateView, UpdateView
from django.forms import ModelForm
from .models import Task


class CustomTaskCreate(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'input-dark', 'autofocus': 'True'})
        self.fields['description'].widget.attrs.update({'class': 'input-dark textarea', 'spellcheck': 'false'})
        self.fields['complete'].widget.attrs.update({'class': 'checkbox-dark'})
        self.fields['show_task'].widget.attrs.update({'class': 'checkbox-dark'})
        self.fields['tags'].widget.attrs.update({'class': 'input-dark select-multiple-field'})

    class Meta:
        model = Task
        fields = ['title', 'description', 'complete', 'show_task', 'tags']


class CustomTaskEdit(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'input-dark'})
        self.fields['description'].widget.attrs.update({'class': 'input-dark textarea', 'spellcheck': 'false'})
        self.fields['complete'].widget.attrs.update({'class': 'checkbox-dark'})
        self.fields['show_task'].widget.attrs.update({'class': 'checkbox-dark'})
        self.fields['tags'].widget.attrs.update({'class': 'input-dark select-multiple-field'})

    class Meta:
        model = Task
        fields = ['title', 'description', 'complete', 'show_task', 'tags']
