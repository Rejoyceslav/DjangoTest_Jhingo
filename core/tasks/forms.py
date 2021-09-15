from django.views.generic.edit import CreateView, UpdateView
from django.forms import ModelForm
from .models import Task, Tag, Folder, Group
from django import forms


class CustomTaskCreate(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # takes 'user' from Views.
        super(CustomTaskCreate, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'input-dark', 'autofocus': 'True'})
        self.fields['description'].widget.attrs.update({'class': 'input-dark textarea', 'spellcheck': 'false'})
        self.fields['complete'].widget.attrs.update({'class': 'checkbox-dark'})
        self.fields['show_task'].widget.attrs.update({'class': 'checkbox-dark'})
        # self.fields['tags'].widget.attrs.update({'class': 'input-dark select-multiple-field'})

        #  find the reason this doesn't allow no fields selected
        self.fields['tags'] = forms.ModelMultipleChoiceField(
            label='Tags',
            queryset=Tag.objects.filter(user=user),
            widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-dark'}),
        )

        self.fields['folder_selected'] = forms.ModelChoiceField(
            label='Folder',
            queryset=Folder.objects.filter(user=user),
            widget=forms.Select(attrs={'class': 'input-dark select-multiple-field'})
        )

        # self.fields['group'] = forms.ModelChoiceField(  # disabled everywhere
        #     label='Group',
        #     queryset=Group.objects.filter(user=user),
        #     widget=forms.Select(attrs={'class': 'input-dark select-multiple-field'})
        # )

    class Meta:
        model = Task
        fields = ['title', 'description', 'complete', 'show_task', 'tags', 'folder_selected']


class CustomTaskEdit(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # takes 'user' from Views.
        super(CustomTaskEdit, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'input-dark'})
        self.fields['description'].widget.attrs.update({'class': 'input-dark textarea', 'spellcheck': 'false'})
        self.fields['complete'].widget.attrs.update({'class': 'checkbox-dark'})
        self.fields['show_task'].widget.attrs.update({'class': 'checkbox-dark'})
        # self.fields['tags'].widget.attrs.update({'class': 'input-dark select-multiple-field'})

        #  find the reason this doesn't allow no fields selected
        self.fields['tags'] = forms.ModelMultipleChoiceField(
            # This was creating a lot of problems. We made changes until it worked
            # MultipleChoiceField doesn't support a queryset argument, so we change the widget to CheckboxSelectMultiple
            label='Tags',
            queryset=Tag.objects.filter(user=user),
            widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-dark'}),
        )

        self.fields['folder_selected'] = forms.ModelChoiceField(
            # ModelChoiceField and ModelMultipleChoiceField accept queryset as an argument
            label='Folder',
            queryset=Folder.objects.filter(user=user),
            widget=forms.Select(attrs={'class': 'input-dark select-multiple-field'})
        )

        # self.fields['group'] = forms.ModelChoiceField(  # disabled everywhere
        #     label='Group',
        #     queryset=Group.objects.filter(user=user),
        #     widget=forms.Select(attrs={'class': 'input-dark select-multiple-field'})
        # )

    class Meta:
        model = Task
        fields = ['title', 'description', 'complete', 'show_task', 'tags', 'folder_selected']


class AddFolderForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'input-dark', 'autofocus': 'True'})

    class Meta:
        model = Folder
        fields = ['name']


class AddTagForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'input-dark', 'autofocus': 'True'})

    class Meta:
        model = Tag
        fields = ['name']


class AddGroupForm(ModelForm):  # disabled everywhere

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'input-dark', 'autofocus': 'True'})

    class Meta:
        model = Group
        fields = ['name']
