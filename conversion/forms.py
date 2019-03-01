from django import forms
from .models import Project, File
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['author', 'project_title', 'date_posted']


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['project', 'author', 'file', 'date_posted']
