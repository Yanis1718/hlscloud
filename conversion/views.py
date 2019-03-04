from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectForm, FileForm
from .models import Project, File
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} !')
            return redirect('create-project')
    else:
        form = UserCreationForm()
    return render(request, 'conversion/register.html', {'form': form})


@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'projects': Project.objects.filter(author=request.user),
                'form': ProjectForm(),
            }
            return render(request, 'conversion/create_project.html', context)
    context = {
        'projects': Project.objects.filter(author=request.user),
        'form': ProjectForm(),
    }
    return render(request, 'conversion/create_project.html', context)


@login_required
def file_list(request, pk):
    files = File.objects.filter(project=pk)
    return render(request, 'conversion/file_list.html', {
        'files': files
    })


def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {
                'projects': Project.objects.filter(author=request.user),
                'form': ProjectForm(),
            }
            messages.success(request, 'Votre fichier à été ajouté au Projet')
            return render(request, 'conversion/create_project.html', context)
    else:
        form = FileForm()
    return render(request, 'conversion/upload_file.html', {
        'form': form
    })


def delete_file(request, pk):
    if request.method == 'POST':
        file = File.objects.get(pk=pk)
        file.delete()
    return redirect('file_list')


def index(request):
    return render(request, 'conversion/base.html')
