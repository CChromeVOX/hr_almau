from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from .models import Project
from .forms import RegistrationForm, StudentLanguageForm, EditProfileForm, ProjectForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def index(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    student = request.user.student
    projects = Project.objects.filter(student=student)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.student = student
            project.save()
            return redirect('profile')  # Перенаправляем на страницу профиля после успешного добавления проекта
    else:
        form = ProjectForm()
    return render(request, 'accounts/profile.html', {'student': student, 'projects': projects, 'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Ваш шаблон для страницы входа
    redirect_authenticated_user = False  # Allow users to access the login page even if authenticated
    next_page = reverse_lazy('main')


@login_required
def edit_profile(request):
    student = request.user.student
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Перенаправляем на страницу профиля после успешного сохранения
    else:
        form = EditProfileForm(instance=student)
    return render(request, 'accounts/edit_profile.html', {'form': form})


@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, id=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'accounts/edit_project.html', {'form': form})

@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('profile')
    return render(request, 'accounts/delete_project.html', {'project': project})



@login_required
def main(request):
    return render(request, 'main.html')



def search_user(request):
    users = User.objects.all()
    user_found = False

    if request.method == "POST":
        search = request.POST.get('search')
        searched_user = User.objects.filter(username__icontains=search).first()
        if searched_user:
            users = [searched_user]
            user_found = True

    return render(request, 'search_user.html', {'users': users, 'user_found': user_found})



def resume(request, user_id):
    user = get_object_or_404(User, id=user_id)
    projects = Project.objects.filter(student=user.student)  # Получаем проекты, связанные с пользователем
    return render(request, 'resume.html', {'user': user, 'projects': projects})