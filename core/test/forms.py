from django.forms import ModelForm
from tasks.models import Task


class TestModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'input-dark'})
        self.fields['description'].widget.attrs.update({'class': 'input-dark', 'spellcheck': 'false'})
        self.fields['complete'].widget.attrs.update({'class': 'checkbox-dark'})
        self.fields['show_task'].widget.attrs.update({'class': 'checkbox-dark'})

    class Meta:
        model = Task
        fields = ['title', 'description', 'complete', 'show_task']






