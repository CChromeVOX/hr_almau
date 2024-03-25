from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student, Faculty, StudentLanguage, Project

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            student = Student.objects.create(user=user)
            print("created")
        return user

class StudentLanguageForm(forms.ModelForm):
    class Meta:
        model = StudentLanguage
        fields = ('language', 'proficiency_level')

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('faculty', 'course', 'profile_photo', 'github')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'photo')